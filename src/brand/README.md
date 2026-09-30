# Casabe mark and lockup

Mark **W3 · seed r 6**: a rounded ink triangle with an orange seed. Source of truth is the Casabe brand kit (its `README.md`); this file records how the workshops site uses it.

## Lockup

**DRAFT, do not ship until the GT Maru license is bought.** `casabe-lockup-currentcolor.svg` is the mark followed by `casabe` outlined from the **trial** font GT Maru Mono Bold. Grilli Type's trial license forbids use in final files, so before this merges the outlines must be regenerated from the licensed font (source: the brand-kit lockup draft, `casabe-lockup-draft/`).

- **Mark:** triangle is `currentColor` (follows the nav/footer text colour, so it flips on dark with no second file); the seed is `style="fill:var(--color--primary)"` (the draft file hardcodes `#e8480c`; it is swapped for the token), so it takes the site's orange and follows the colour switch. The build inlines the SVG into each page, which is what lets the variable resolve; the file on its own (opened as an image) renders the seed black. Geometry is the kit's `mark/casabe-mark.svg`.
- **Wordmark:** five-letter `casabe` outlines, `currentColor`, in one path.
- **Proportions (B+):** the mark's bottom sits on the text baseline; the mark is as tall as the "b" plus 4%; the gap between mark and "c" equals the seed's diameter; lockup width = mark height x 6.9. viewBox is `0 -1522 10503 1552`: the mark spans 1522 units, the extra 30 is the descender of the "c" and "e" overshoot below the baseline.
- **Sizes on the site:** the SVG height is the mark height x 1552/1522 (x 1.0197), set in `src/body.html`, `src/progress.html`, `src/sign.html`.

  | Place | Mark | SVG height | Width |
  |---|---|---|---|
  | Nav, 768px and up | 30px | 30.6px | 207px |
  | Nav, below 768px | 22px | 22.4px | 152px (same as the old lockup) |
  | Footer, 768px and up | 32px | 32.6px | 221px |
  | Footer, below 768px | 24px | 24.5px | 166px |
  | QR sign | 32px | 32.6px | 221px |

  At 375px a 24px mark (166px wide) overflowed the nav links by 9px, so the nav mark is 22px there; at 375px the links have 5px to spare. At 360px the nav links still overflow by 10px (the old lockup was the same width, so this is unchanged).

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
