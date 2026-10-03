# Casabe mark and lockup

Mark **W3, knockout**: a rounded triangle with a seed-sized hole cut through it. Source of truth is the Casabe brand kit (its `README.md`); this file records how the workshops site uses it.

## Lockup

`casabe-lockup-currentcolor.svg` is the kit's `wordmark/casabe-lockup.svg` (outlined GT Maru Mono Bold, no font file needed) with three changes: fills are `currentColor` instead of `#16161a`, the c2pa `<metadata>` block and its namespace are stripped, and the fixed `width`/`height` are dropped so CSS sizes it. Check that the GT Maru license covers logo use before shipping (kit note).

- **One color.** The seed is a hole (`fill-rule="evenodd"`), not a second shape, so the background shows through it: paper on light, ink on dark. The mark and wordmark follow the text color, so the lockup flips on dark with no second file. There is no orange seed.
- **Proportions (kit):** mark height = 0.86x the font size, mark on the baseline, gap = 0.3x the font size. viewBox `0 0 485.72 81.91`, so width = height x 5.93.
- **`build.py`** injects the file at `<!--LOCKUP-->`, adding the `brand-lockup` class, and asserts the evenodd hole is present, the fills are `currentColor` and no c2pa data remains (there is no seed element to assert on any more).
- **Sizes on the site** (SVG height; measured in the built pages):

  | Place | SVG height | Width |
  |---|---|---|
  | Nav, 768px and up | 34px | 201.6px |
  | Nav, below 768px | 25px | 148.2px |
  | Footer, 768px and up | 36px | 213.5px |
  | Footer, below 768px | 28px | 166px |
  | QR sign | 36px | 213.5px |

  At 375px the nav is lockup 148px + Materials + Steps + theme toggle, and the toggle's right edge is at 359px (16px page padding), with the links list not scrolling (scrollWidth equals clientWidth).

## Clear space and minimum size (from the kit)

- Clear space equals the seed's diameter on all sides.
- Minimum 16px tall on screen. At 24px and below use the small mark (`mark/small/` in the kit; the favicons already do). Never use the small mark above 32px.
- Don't recolor, stretch, rotate, outline or add effects. Don't move the seed.

## Color

| Token | Hex |
|---|---|
| Ink | `#16161a` |
| Paper | `#f7f7f8` |
| Orange | `#e8480c` |

The logo is always one color. Orange stays the accent for buttons, highlights and step numerals; the workshops CSS uses the tokens (`--color--primary`, `--color--ink-fixed`, the `--direction--*-dark` surfaces) and holds no orange or ink hex of its own. The built pages inline batey-platform's `site/styles.css`.

Accessibility (kit rules): small text is never orange on a light background (`#e8480c` on `#f7f7f8` is 3.66:1); buttons are ink text on orange; orange text is fine on dark. The large bold step numerals (24px, 26px on the QR sign) are the only orange text on light and pass the 3:1 large-text bar.

## Icons (`assets/brand/`, from the kit's `icons/`)

`favicon.svg` (kit file, which already uses the small mark with the r 7 hole, plus a `prefers-color-scheme` style so the triangle is ink on light tabs and paper on dark; the kit file had no fill, so it rendered black, and its c2pa metadata is stripped), `favicon-16/32/48.png`, `apple-touch-icon.png`, `icon-192/512.png`, `icon-maskable-512.png` (all copied from the kit), `site.webmanifest` (kit file with icon paths made absolute). `build.py` links the SVG, the 32px PNG, the apple-touch icon and the manifest in every page head.
