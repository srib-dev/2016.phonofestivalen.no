# JavaScript sources (BaseKit / Webhuset)

Vendored for offline/local serving of the Phonofestivalen 2016 mirror.

| File | CDN URL | Notes |
|------|---------|--------|
| `published-site.js` | `http://55b558c7-resources.basekit.webhuset.no/6146dd5/compiled/published-site.js` | Main runtime (jQuery, PhotoSwipe, widgets, nav). |
| `published-site-jquery-lightbox.js` | `…/6146dd5/compiled/published-site-jquery-lightbox.js` | Not on CDN (404, 2026); captured via [Wayback `js_` replay](https://web.archive.org/web/20160601055215js_/http://55b558c7-resources.basekit.webhuset.no/6146dd5/compiled/published-site-jquery-lightbox.js), wombat wrapper removed. |
| `twig-widget-views-v1.js` | `…/6146dd5/compiled/twig-widget-views-v1.js` | Widget view bootstrap. |
| `translations.js` | `…/7e634a0/no/translations.js?sections=widgets,mobile,shared_views,shared_components,cookie` | Norwegian UI strings. |
| `fonts/6146dd5-montserrat.woff.json` | `…/6146dd5/seven/fonts/montserrat.woff.json` | Webfont cache for `js-webfont` (most pages). |
| `fonts/6146dd5-montserrat.ttf.json` | `…/6146dd5/seven/fonts/montserrat.ttf.json` | Same. |
| `fonts/c9d240e-montserrat.woff.json` | `…/c9d240e/seven/fonts/montserrat.woff.json` | Home page bundle id (`Phonofestivalen.html`). |
| `fonts/c9d240e-montserrat.ttf.json` | `…/c9d240e/seven/fonts/montserrat.ttf.json` | Same. |

`6146dd5` and `c9d240e` `published-site.js` builds are byte-identical; only one copy is kept.

Load order in HTML: `published-site-jquery-lightbox.js` (most pages) → `translations.js` → `published-site.js` → `twig-widget-views-v1.js`.
