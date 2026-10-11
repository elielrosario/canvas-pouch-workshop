# Casabe mark and lockup

Mark **W03, the line mark**, the primary Casabe logo (owner decision, 2026-10-10): an open-base triangle drawn as a line, with a door in the base and a filled seed. Source of truth is the Casabe brand kit's `line-mark/` folder (its `README.md`); this file records how the workshops site uses it.

## Lockup

`casabe-lockup-currentcolor.svg` is the kit's `line-mark/casabe-line-lockup-ink.svg` (outlined GT Maru Mono Bold, no font file needed) with three changes: the stroke and fills are `currentColor` instead of `#16161a`, the c2pa `<metadata>` block and its namespace are stripped, and the fixed `width`/`height` are dropped so CSS sizes it. Check that the GT Maru license covers logo use before shipping (kit note).

- **One color.** The triangle is a stroke (line 6, round joins and ends) and the seed (r 4) is a filled circle in the same color, not a hole. The mark and wordmark follow the text color, so the lockup flips on dark with no second file. There is no orange seed.
- **Proportions (kit):** mark height = 0.86x the font size, mark on the baseline, gap = 0.3x the font size (0.2993x). viewBox `0 -9.376 486.373 81.876`, so width = height x 5.94.
- **`build.py`** injects the file at `<!--LOCKUP-->`, adding the `brand-lockup` class, and asserts the stroke (`stroke="currentColor"`, width 6) and the seed circle are present and no c2pa data remains.
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
- At 24px and below use the small line mark (`line-mark/small/` in the kit; the favicons already do). The workshops lockup is never drawn that small.
- Don't recolor, stretch, rotate, outline or add effects. Don't move the seed.

## Color

| Token | Hex |
|---|---|
| Ink | `#16161a` |
| Paper | `#f7f7f8` |
| Orange | `#e8480c` |

The logo is always one color. Orange stays the accent for buttons, highlights and step numerals; the workshops CSS uses the tokens (`--color--primary`, `--color--ink-fixed`, the `--direction--*-dark` surfaces) and holds no orange or ink hex of its own. The built pages inline batey-platform's `site/styles.css`.

Accessibility (kit rules): small text is never orange on a light background (`#e8480c` on `#f7f7f8` is 3.66:1); buttons are ink text on orange; orange text is fine on dark. The large bold step numerals (24px, 26px on the QR sign) are the only orange text on light and pass the 3:1 large-text bar.

## Icons (`assets/brand/`, from the kit's `line-mark/icons/`)

`favicon.svg` (kit file: the small line mark with a `prefers-color-scheme` style, so the triangle is ink on light tabs and paper on dark), `favicon-16/32/48.png`, `apple-touch-icon.png`, `icon-192/512.png`, `icon-maskable-512.png` (all copied from the kit; same sizes as before), `site.webmanifest` (kit file with icon paths made absolute; unchanged). `build.py` links the SVG, the 32px PNG, the apple-touch icon and the manifest in every page head.
