# Publisher website guide

Maintain **Oberasoftware Publishing** as a portfolio of independently built games and software. Current products are Haven Under Fire and JasDB; Train Studio is reserved but unpublished.

Keep the website static, accessible and responsive. Edit `tools/build.py` and `_data/products.json`, regenerate HTML, run `python3 tools/check_site.py`, then visually inspect desktop/mobile/tablet. Preserve `CNAME`, `/api/` and app-linked `/haven-under-fire/` and `/haven-under-fire/privacy/` URLs. `/jasdb/` belongs to the separate legacy project site; the modern product page lives at `/products/jasdb/`.

Use authentic product media, clearly distinguish artwork/diagrams from actual gameplay, retain provenance in MEDIA.md, and optimize file size without misrepresenting the product. Never invent availability, prices, store/test links, download buttons, testimonials or compatibility. New products join the catalogue only when enough approved detail exists.

No tracking, third-party scripts, external fonts, cookies or backend without explicit approval. Keep privacy accurate for both local game data and GitHub Pages hosting. Do not modify unrelated product repositories, game code or signing settings. Publish only the reviewed static-site commit; never commit credentials or local QA output.
