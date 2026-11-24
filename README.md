# Oberasoftware Publishing

Static publisher site at **https://www.oberasoftware.com**. Two published product pages: Haven Under Fire and JasDB. The existing `CNAME` and JasDB API documentation are preserved.

## Edit and preview

- Product catalogue: `_data/products.json` (only `published: true` entries appear).
- Page content/templates: `tools/build.py`.
- Shared design and optional screenshot viewer: `assets/publishing/`.
- Media: `assets/products/` with provenance in `MEDIA.md`.

```sh
python3 tools/build.py
python3 tools/check_site.py
python3 -m http.server 5201 --bind 127.0.0.1
```

Review desktop, 390px phone and tablet. Check navigation, support accordions, keyboard focus and screenshot viewer (Escape, Previous/Next, focus return). Plain HTML links remain usable with JavaScript disabled. Commit generated HTML alongside its templates; GitHub Pages serves the repository without a package install or app backend.

## Publishing and stable addresses

GitHub Pages publishes the root of the `master` branch. `.nojekyll` keeps the generated pages static. Keep `CNAME` equal to `www.oberasoftware.com`. Push the reviewed commit to that branch, wait for the Pages deployment, then check the public URLs over HTTPS.

- `/`: publisher collection.
- `/haven-under-fire/`: game landing page and prominent support links. This is the **support URL already embedded in the app and App Store Connect**.
- `/haven-under-fire/support/`: player FAQ.
- `/haven-under-fire/privacy/`: stable game privacy URL already embedded in the app/store.
- `/products/jasdb/`: new JasDB product page. `/jasdb/` is an existing separately published project documentation site; do not shadow it here.
- `/api/`: retained historical JasDB Java API.
- `/support/`, `/privacy/`: publisher-wide help/privacy.

Only Haven Under Fire and JasDB are promoted. Retired services, HomeAutomation and personal profiles are absent from the new UI. Old unused assets remain for URL compatibility; they are not loaded by the new pages. No old analytics or social widgets are loaded.

## Future products

Train Studio has an unpublished catalogue stub. Add its approved description, status, platform, page URL, media and a dedicated page in the generator before setting `published: true`. No invented features, dates, availability or store links. Add future products to the footer/support pages and sitemap when they ship.

## Release accuracy

Haven Under Fire is **in beta**, not publicly released. The launch model is one free land, a €3.99 euro Full Game unlock for seven additional campaign lands through progression and Custom Game. When the App Store listing is live, replace the coming-soon text with a verified store link; no fake Download or public TestFlight link is present.

JasDB source currently describes a Java 17 / 2.0 development branch without published 2.0 artifacts. Existing documentation is for the older release. Recheck the upstream README before changing those claims. Link the actual license (which includes an additional redistribution condition); do not call it unmodified MIT.

The website is static and contains no telemetry, cookies, forms, remote fonts or embedded third-party media. GitHub hosting security logs are described separately from the game's local data handling.

## Redesign validation — 24 November 2026

The eight generated pages passed local link/anchor, metadata, image and catalogue checks. Browser review covered desktop (1440px), tablet (834px), phone (390px) and narrow phone (320px), with no page overflow. Screenshot navigation, arrow keys, Escape/focus return and the support accordion were exercised. Mobile navigation has 44px-tall targets. Product media totals approximately 2.4 MiB; responsive images and lazy loading keep initial transfers smaller. No product runtime or existing documentation was changed.
