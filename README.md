# Bridge Con website

The public pages App Store Connect needs for **Bridge Con**: a landing page,
the **privacy policy** and the **support** page, in English (`/`), Ukrainian
(`/uk/`) and Russian (`/ru/`).

## Before deploying

Open `build.py` and set (`SITE_BASE` is set by the GitHub workflow):

- `SUPPORT_EMAIL` — the address users write to;
- `APP_STORE_URL` — the App Store link, once the app is live (until then the
  page says "Coming soon").

`python3 -I build.py` builds the site into `public/` to look at locally
(`open public/index.html`, or `python3 -m http.server -d public`).

## Live on GitHub Pages

Every push to `main` builds the site (`.github/workflows/pages.yml`) and
publishes it at **https://racot86.github.io/bridgecon-site/**.

## Or deploy with Coolify

1. New resource → this Git repository → build pack **Dockerfile**.
2. Port **80**. Add your domain (e.g. `bridgecon.example.com`) and let Coolify
   issue the HTTPS certificate.
3. Deploy. The Dockerfile builds the pages itself; `public/` isn't committed.

## URLs for App Store Connect

| Field | URL |
|---|---|
| Privacy Policy URL | `https://<domain>/privacy` |
| Support URL | `https://<domain>/support` |
| Marketing URL | `https://<domain>/` |

Ukrainian and Russian pages: add `uk/` or `ru/` after the domain.
