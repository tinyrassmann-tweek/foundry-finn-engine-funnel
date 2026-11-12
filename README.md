# Foundry Finn Engine & Funnel

Independent, Hallmark-inspired acquisition frontend for the 12-venture Think Tank Solutions AI ecosystem. This package contains no report-generation engine, API credentials, or production deployment changes. All report calls to action link to the existing live application.

## Run locally

`python3 -m http.server 8080` then open `http://localhost:8080/`. Open `/banner-preview.html` for the banner.

## Install the shared banner

Add `components/banner.css` to each public layout, then insert the matching venture HTML snippet from `components/`. The twelve slugs and entry URLs are defined in `config/ventures.json`. Preserve source attribution; do not place this banner inside private dashboards, checkout, or sensitive workflows. Do not auto-redirect visitors. The links work without JavaScript.

## Integration boundary

The actual deployed report source was not available for inspection. The similarly named older GitHub repo only queues local submissions. Do not deploy it over production. This repo does not contain, reproduce, or replace the live generator. Preserve report completion, downloads, data contracts, consent, and existing integration behavior. Verify the production source, parent URL, and post-report handoff before adding an optional Think Tank Solutions AI CTA to the report completion screen. The parent URL is intentionally null in the manifest rather than guessed. UTM tags identify entry sources but actual attribution collection requires verified analytics integration.

## Acceptance gates

- `python3 tests/check.py` validates 12 unique entries, separate ancestry brands, local anchors, and the matching report destination in each snippet.
- Verify the live report route in a browser, submit an approved test business, and inspect the complete output and download behavior before modifying production.
- Run Hallmark's browser audit against the true app source before release; this independent preview is Hallmark-inspired, not a certified full Hallmark run.
- Verify the parent hub URL, post-report CTA, and analytics attribution; never put business descriptions or personal data into tracking URLs.
- Deploy separately as a preview first. Keep the original live URL and engine unchanged.

## Upstream design reference

https://github.com/nutlope/hallmark
