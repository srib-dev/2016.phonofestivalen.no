#!/usr/bin/env python3
"""Point in-repo navigation and phonofestivalen URLs at local HTML files."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

SLUG_TO_FILE = {
    "": "Phonofestivalen.html",
    "program": "Program.html",
    "artister": "Artister.html",
    "kunst-og-kultur": "Kunst og Kultur.html",
    "frivillig": "Frivillig.html",
    "billetter": "Billetter.html",
    "galleri": "Galleri.html",
    "info": "Info.html",
    "nyheter": "Phonofestivalen.html",
    "artistslipp3": "Artistslipp#3.html",
    "artistslipp-3": "Artistslipp#3.html",
    "artistslipp-1": "Artistslipp #1.html",
    "artistslipp-2": "Artistslipp #2.html",
    "antler": "Antler.html",
    "baby-in-vain": "Baby In Vain.html",
    "bendik": "Bendik.html",
    "haust": "Haust.html",
    "hester-v75": "Hester V75.html",
    "karokh": "Karokh.html",
    "marinius": "Marinius.html",
    "marte-eberson": "Marte Eberson.html",
    "simen-mitlid": "Simen Mitlid.html",
    "slutface": "Slutface.html",
    "westkust": "Westkust.html",
    # No Wayback capture; link to parent section in mirror
    "hoes-of-techno": "Artister.html",
    "klubbkveld": "Artister.html",
    "kulturelle-toner": "Kunst og Kultur.html",
    "panelsamtale": "Kunst og Kultur.html",
    "kunstutstilling": "Kunst og Kultur.html",
}

CANONICAL_FOR_FILE = {v: k for k, v in SLUG_TO_FILE.items() if k != "nyheter"}
CANONICAL_FOR_FILE["Phonofestivalen.html"] = ""


def local_for_url(url: str) -> str | None:
    url = url.strip()
    if url.startswith("http://editor.wsb.webhuset.no/"):
        slug = url.rstrip("/").split("/")[-1].lower()
        return SLUG_TO_FILE.get(slug)
    for host in ("http://www.phonofestivalen.no/", "https://www.phonofestivalen.no/"):
        if url.startswith(host):
            slug = url[len(host) :].split("?")[0].strip("/").lower()
            return SLUG_TO_FILE.get(slug)
    if url.startswith("https://web.archive.org/web/") and "phonofestivalen.no/" in url:
        m = re.search(r"phonofestivalen\.no/([^/?\"]+)", url)
        if m:
            return SLUG_TO_FILE.get(m.group(1).lower())
    return None


def fix_html(text: str, filename: str) -> str:
    n = text

    n = re.sub(r'href="http://mailto:', 'href="mailto:', n)

    # Broken Wayback-wrapped social (Billetter)
    n = n.replace(
        'href="https://web.archive.org/web/20160601053527/https://twitter.com/https://twitter.com/phonofestivalen"',
        'href="https://x.com/phonofestivalen"',
    )
    n = n.replace(
        'href="https://web.archive.org/web/20160601053527/https://www.facebook.com/pages/Phonofestivalen/46344175404?fref=ts"',
        'href="Info.html#facebook"',
    )

    # Footer Twitter → X; Facebook → local Info anchor
    n = n.replace(
        'href="https://twitter.com/phonofestivalen"',
        'href="https://x.com/phonofestivalen"',
    )
    n = n.replace(
        'href="https://www.facebook.com/pages/Phonofestivalen/46344175404?fref=ts"',
        'href="Info.html#facebook"',
    )

    # SRIB: keep on Info page where festival is described
    n = n.replace('href="http://www.srib.no/"', 'href="Info.html"')

    def repl_href(m: re.Match[str]) -> str:
        quote = m.group(1)
        url = m.group(2)
        local = local_for_url(url)
        if local:
            return f"href={quote}{local}{quote}"
        return m.group(0)

    n = re.sub(r'href=(["\'])(https?://[^"\']+)\1', repl_href, n)

    # Remove empty duplicate anchors (editor stubs with no text)
    n = re.sub(
        r'<a href="[^"]+\.html" target="_self"><span style="color: rgb\(192, 80, 77\);"></span></a>',
        "",
        n,
    )
    # Merge duplicate artistslipp#3 link on home: keep text link only
    n = re.sub(
        r'<a href="Artistslipp#3\.html" target="_self"><span style="color: rgb\(192, 80, 77\);"></span></a>',
        "",
        n,
    )

    # Canonical + og:url → local file
    canon_file = filename
    if filename in CANONICAL_FOR_FILE or filename.endswith(".html"):
        n = re.sub(
            r'<link rel="canonical" href="[^"]*">',
            f'<link rel="canonical" href="{canon_file}">',
            n,
            count=1,
        )
        n = re.sub(
            r'<meta property="og:url" content="[^"]*">',
            f'<meta property="og:url" content="{canon_file}">',
            n,
            count=1,
        )

    # Billetter embedded JSON (Wayback leftovers)
    n = n.replace(
        "https:\\/\\/web.archive.org\\/web\\/20160601053527\\/https:\\/\\/twitter.com\\/phonofestivalen",
        "https:\\/\\/x.com\\/phonofestivalen",
    )
    n = n.replace(
        "https:\\/\\/web.archive.org\\/web\\/20160601053527\\/https:\\/\\/www.facebook.com\\/pages\\/Phonofestivalen\\/46344175404?fref=ts",
        "Info.html#facebook",
    )
    n = n.replace(
        '\\/\\/web.archive.org\\/web\\/20160601053527\\/http:\\/\\/resizer.basekit.webhuset.no\\/webhuset2925\\/image\\/logo-w.png?w=960',
        "images\\/logo-w.png",
    )
    n = n.replace(
        "https:\\/\\/web.archive.org\\/web\\/20160601053527\\/http:\\/\\/files.basekit.webhuset.no\\/webhuset2925\\/image\\/02facebook-banner2.png",
        "images\\/02facebook-banner2.png",
    )

    return n


def main() -> None:
    for path in sorted(ROOT.glob("*.html")):
        original = path.read_text(encoding="utf-8")
        updated = fix_html(original, path.name)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print("updated", path.name)


if __name__ == "__main__":
    main()
