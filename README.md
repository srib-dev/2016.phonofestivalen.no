# 2016.phonofestivalen.no
Gjenskapelse av Phonofestivalen sin nettside i 2016, basert på filer funnet i Internet Archive

## Kjøre lokalt
Åpne **ikke** bare filer med `file://` hvis du vil ha normal CSS/JS-oppførsel (nettleseren blokkerer ofte script og relative stier på forskjellige måter).

Fra denne mappen:

```bash
python3 -m http.server 8765
```

Åpne deretter [http://127.0.0.1:8765/Phonofestivalen.html](http://127.0.0.1:8765/Phonofestivalen.html) (eller en annen `.html`-side).

- **CSS** ligger i `css/` (hovedstil: `site_2925_44_122.css`).
- **Bilder** ligger i `css/../images/`.
- **JavaScript** (BaseKit-malen) ligger i `js/` — navigasjon, mobilmeny og lightbox avhenger av disse. Opprinnelige URL-er: `js/SOURCES.md`. Montserrat-cache: `js/fonts/`.

Noen mal-bilder i CSS peker ikke på lokale filer; layouten kan da se litt «flatt» ut, men tekst og struktur skal fortsatt være lesbare.

## Publisering (GitHub Pages → 2016.phonofestivalen.no)

Dette repoet er statisk og passer GitHub Pages. Målet er at nettsiden skal ligge på **https://2016.phonofestivalen.no/** (ikke bare `srib-dev.github.io/…`).

### I GitHub (repo `srib-dev/2016.phonofestivalen.no`)

1. **Settings → Pages**
2. **Source**: Deploy from branch **`main`**, mappe **`/ (root)`**
3. **Custom domain**: `2016.phonofestivalen.no` (lagres også i [`CNAME`](CNAME) i repoet)
4. Vent til DNS er OK (grønn hake), slå på **Enforce HTTPS**

### DNS (hos domeneleverandør for `phonofestivalen.no`)

Legg inn én **CNAME**-post (subdomene, ikke apex):

| Type  | Navn / host | Mål / verdi           |
|-------|-------------|------------------------|
| CNAME | `2016`      | `srib-dev.github.io`   |

Noen paneler ber om fullt navn `2016.phonofestivalen.no` i stedet for bare `2016` — bruk det leverandøren forventer. **Ikke** pek subdomenet mot `srib-dev.github.io/2016.phonofestivalen.no`; det skal være **`srib-dev.github.io`**.

Propagering kan ta fra minutter til et døgn. GitHub sjekker at CNAME er riktig før sertifikat og grønn hake.

### Etter oppdatering

- Forside: **https://2016.phonofestivalen.no/** (`index.html` → `Phonofestivalen.html`)
- Relative lenker (`Program.html`, `images/…`, `js/…`) fungerer på roten av subdomenet uten ekstra konfigurasjon

`.nojekyll` i roten hindrer at GitHub/Jekyll ignorerer filer under `js/` m.fl.
