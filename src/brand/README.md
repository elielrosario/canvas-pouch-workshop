# Casabe mark and lockup

The Casabe logo (new, owner-approved 2026-11-17): a solid triangle with rounded corners and a round seed, beside the new rounded uppercase letters CASABE. Source of truth is the Casabe brand kit (`brand/casabe-brand-kit/` in batey-platform; its `README.md`). The shapes are never altered.

## Lockup

`casabe-lockup-currentcolor.svg` is the kit's `lockup/casabe-lockup-ink.svg` with the one change that its fill is `currentColor` instead of `#16161a`; geometry is identical (viewBox `0 0 85 16`, width = height x 5.3125). CSS sizes it.

- **The seed is a hole.** The triangle and circle are one path with `fill-rule="evenodd"`, so the background shows through. Never put a colored dot in it.
- **One color.** Follows the text color, so it flips on dark with no second file.
- **`build.py`** injects the file at `<!--LOCKUP-->`, adding the `brand-lockup` class, and asserts the evenodd path, the viewBox and `currentColor` are present with no stroke.
- **Sizes on the site** (SVG height; mark height kept close to the old line mark's):

  | Place | SVG height | Width |
  |---|---|---|
  | Nav, 768px and up | 30px | 159.4px |
  | Nav, below 768px | 22px | 116.9px |
  | Footer, 768px and up | 32px | 170px |
  | Footer, below 768px | 25px | 132.8px |
  | QR sign | 32px | 170px |

## Clear space and minimum size (kit)

No small-size optical cut exists: at 16px the hole is about 2px wide. Don't recolor, stretch, rotate, outline or add effects.

## Color

Ink `#16161a`, Paper `#f7f7f8`, Orange `#e8480c`. The logo is always one color; orange stays the accent for buttons, highlights and step numerals.

## Icons (`assets/brand/`, from the kit's `icons/`)

`favicon.svg` (ink, paper in dark mode), `favicon-16/32/48.png`, `apple-touch-icon.png`, `icon-192/512.png`, `icon-maskable-512.png` are copied from the kit unchanged. `site.webmanifest` keeps absolute icon paths (otherwise the kit file). `build.py` links them in every page head.
