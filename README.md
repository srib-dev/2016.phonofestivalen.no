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
