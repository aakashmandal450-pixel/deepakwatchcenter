# Deepak Watch Center website

Static website for Deepak Watch Center, Bus Park Road, Dhangadhi.

- No build step, no dependencies, no database, no cookies, no tracking.
- `build.py` regenerates `index.html`, `privacy.html`, `terms.html` and `404.html` from one template: `python3 build.py`.
- `_headers` sets security headers (CSP, HSTS, no framing) when hosted on Cloudflare Pages.
- Image credits: `assets/img/CREDITS.md`.

## Hosting on Cloudflare Pages

1. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → choose this repository.
2. Framework preset: None. Build command: (leave empty). Output directory: `/`.
3. After the first deploy, add the custom domain `deepakwatchcenter.com.np` under the project's Custom domains.
