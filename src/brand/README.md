# Casabe mark and lockup

Mark **W3 · seed r 6**: a rounded ink triangle with an orange seed. Source of truth is the Casabe brand kit (its `README.md`); this file records how the workshops site uses it.

## Lockup

`casabe-lockup-currentcolor.svg` is the mark followed by the `Casabe` wordmark.

- **Mark:** triangle is `currentColor` (follows the nav/footer text colour, so it flips on dark with no second file); the seed is fixed orange `#e8480c`. Geometry is the kit's `mark/casabe-mark.svg`, metadata stripped.
- **Wordmark:** the vectorised Familjen Grotesk 700 paths from the previous lockup, **unchanged**. The kit ships no wordmark because GT Maru is not yet licensed. When it is, outline the lockup from the licensed font and replace only the wordmark group.
- **Layout (viewBox 6326 x 1100):** mark height 1100, mark bottom edge on the wordmark baseline, mark 1.1x the cap height, gap 200 (about two thirds of the seed diameter 292). The apex sits 86 above the cap line.
- **Sizes on the site:** 30px tall in the nav, 32px in the footer and on the QR sign (set in `src/body.html`, `src/progress.html`, `src/sign.html`).

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

The site stylesheet's own primary is `#f1511b` (from `batey-platform/site/styles.css`), which differs from the kit's orange. The site tokens are left as they are.

## Icons (`assets/brand/`, from the kit's `icons/`)

`favicon.svg` (kit file plus a `prefers-color-scheme` style so the triangle is ink on light tabs and paper on dark; the kit file had no fill, so it rendered black), `favicon-16/32/48.png`, `apple-touch-icon.png`, `icon-192/512.png`, `icon-maskable-512.png`, `site.webmanifest` (icon paths made absolute). `build.py` links the SVG, the 32px PNG, the apple-touch icon and the manifest in every page head.
