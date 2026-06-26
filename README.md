# Australian Sports Brain Bank — website (re-skin draft)

A static, multi-page re-skin of brainbank.org.au. Plain HTML/CSS/JS — no build step, no framework. Open `index.html` in a browser to preview locally.

## Pages
- `index.html` — Home
- `about.html` — About Us (team + ambassadors)
- `why-pledge.html` — Why pledge
- `make-a-pledge.html` — Make a pledge (links to the REDCap ethics-approved form)
- `cte-diagnosis.html` — CTE diagnosis statement
- `cte-research.html` — CTE research
- `publications.html` — Our publications
- `partners.html` — Partners & supporters
- `support.html` — Support us
- `resources.html` — Resources hub (CTE info + downloadable PDFs)
- `contact.html` — Contact
- `assets/styles.css`, `assets/site.js` — shared styles and nav script
- `_gen.py` — optional build script used to generate the inner pages (not needed to run the site)

## Deploy on GitHub Pages (gets you a usable link)
1. Create a new GitHub repository (e.g. `asbb-website`).
2. Upload **all** files in this folder, keeping the `assets/` folder structure intact (so `index.html` and `assets/` sit at the repo root).
3. In the repo: **Settings → Pages**.
4. Under "Build and deployment", Source = **Deploy from a branch**, Branch = **main**, folder = **/ (root)**. Save.
5. Wait ~1 minute. Your link appears at the top of the Pages settings, e.g. `https://<your-username>.github.io/asbb-website/`.

The included `.nojekyll` file tells GitHub to serve the files as-is.

## Important notes on images (read before going live)
- **Hero, microscope and community photos** are currently referenced from an external image CDN as AI-generated placeholders. They render fine over the web, but for production permanence they should be **downloaded into `assets/img/` and the URLs updated**, and ideally replaced with the client's licensed photography.
- **Partner logos** are pulled from the charity's existing live site CDN. Same recommendation: save the official logo files into `assets/img/` and point to them locally.
- **Team headshots** are placeholder initials until Alan's standardised photo set is supplied.

## External links (kept external, unchanged UX)
- Donate: `https://www.mycause.com.au/charity/47696/AustralianSportsBrainBank`
- Pledge (NSW Health ethics-approved): `https://redcap.slhd.nsw.gov.au/surveys/?s=HJFCHCHHL8JELFMH`
- E-newsletter signup: `https://greenarrow.health.nsw.gov.au/ga/front/forms/114/subscriptions/new/`
