# Casabe mark and lockup

Mark **W3 · seed r 6**: a rounded ink triangle with an orange seed. Source of truth is the Casabe brand kit (its `README.md`); this file records how the workshops site uses it.

## Lockup

`casabe-lockup-currentcolor.svg` is the mark followed by the lowercase outlined `casabe` wordmark, laid out the way the casabe.studio nav does it.

- **Mark:** triangle is `currentColor` (follows the nav/footer text colour, so it flips on dark with no second file); the seed is `style="fill:var(--color--primary)"`, so it takes the site's orange token (`#e8480c`) and follows the colour switch. The build inlines the SVG into each page, which is what lets the variable resolve; the file on its own (opened as an image) has no `--color--primary` and renders the seed black. Geometry is the kit's `mark/casabe-mark.svg`, metadata stripped.
- **Wordmark:** the five outlined `casabe` paths from batey-platform's nav package (`packages/nav/src/index.ts`, `WORDMARK_PATH_0..4`, PR #425), all `currentColor`, each keeping its own fill rule (the `s` overlap slivers are nonzero, the counters in `a`/`b`/`e` are evenodd). Copy them from there rather than redrawing; when the nav wordmark changes, replace the nested wordmark `<svg>` here.
- **Layout (viewBox 162.4 x 32):** the nav's own numbers at a 32 unit mark height. Mark 36.4 x 32 (kit viewBox `6.3 9.4 51.4 45.2`), gap 12.5, wordmark 113.5 x 26.9 (viewBox `44.5 104.5 1268.5 302`), bottoms aligned (the nav uses `align-items: flex-end`). No padding in the box, so the mark renders at the full lockup height.
- **Sizes on the site:** 30px tall in the nav (152px wide), 32px in the footer and on the QR sign (162px wide) (set in `src/body.html`, `src/progress.html`, `src/sign.html`). At 375px the nav still fits "Materials", "Steps" and the theme button without clipping.

`build.py` injects the file at `<!--LOCKUP-->`, adding the `brand-lockup` class.

## Clear space and minimum size (from the kit)

- Clear space equals the seed's diameter on all sides.
- Minimum 16px tall on screen. Below 24px use the ink/paper mark with the orange seed; never the knockout, the hole closes up.
- Don't recolour, stretch, rotate, outline or add effects. Don't move the seed.

## Colour

| Token | Hex |
|---|---|
| Ink | `#16161a` |
| Paper | `#f7f7f8` |
| Orange (seed) | `#e8480c` |

The built pages inline batey-platform's `site/styles.css`, whose `--color--primary` is the kit orange `#e8480c` on the `claude/kit-colours` branch. The workshops CSS uses the tokens (`--color--primary`, `--color--ink-fixed`, the `--direction--*-dark` surfaces) and holds no orange or ink hex of its own.

Accessibility (kit rules): small text is never orange on a light background (`#e8480c` on `#f7f7f8` is 3.66:1); buttons are ink text on orange; orange text is fine on dark. The large bold step numerals (24px, 26px on the QR sign) are the only orange text on light and pass the 3:1 large-text bar.

## Icons (`assets/brand/`, from the kit's `icons/`)

`favicon.svg` (kit file plus a `prefers-color-scheme` style so the triangle is ink on light tabs and paper on dark; the kit file had no fill, so it rendered black), `favicon-16/32/48.png`, `apple-touch-icon.png`, `icon-192/512.png`, `icon-maskable-512.png`, `site.webmanifest` (icon paths made absolute). `build.py` links the SVG, the 32px PNG, the apple-touch icon and the manifest in every page head.
