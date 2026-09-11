# Casabe — Partido Mark · Production Spec

Locked 2026-09-11. Source of truth for geometry is this document; the lab (`casabe-partido-lab.html`, preset "Módulo 10" with module set to 12) regenerates it.

## Geometry

Mark box: **100 × 89** units, no padding. All values on a single module **m = 12**.

| Element | Value |
|---|---|
| Block | x 8–92 (84 wide) · y 0–58 (58 tall) · square corners |
| Triangle counter (void) | apex (50, 12) · base y 46 · half-width 25.16 · height 34 |
| Clearance around triangle | top 12 · bottom 12 · sides 16.84 (derived) |
| Slope | half-width ÷ height = **0.74** (same as the CP mark) |
| Gap block → bar | 12 |
| Bar | x 8–92 · y 70–89 (19 = m × 1.6) · square corners |

Paths (evenodd for the block):

```
Block + counter:  M8 0 H92 V58 H8 Z  M50 12 L75.16 46 L24.84 46 Z
Bar:              M8 70 H92 V89 H8 Z
```

The counter is a true knockout — the surface shows through it. Never paint it.

## Lockups

**Horizontal.** The mark's **block top sits on the cap line and the bar's top edge sits on the baseline** — the word stands on the bar, and the bar hangs below the baseline as foundation. This makes the mark 1.271× the cap height and puts its ink centroid within 3 units of the wordmark's (measured; the bar-bottom-on-baseline alternative left the mark a quarter cap-height too high). Gap between mark and wordmark = 1.5 modules at lockup scale.

**Stacked.** Mark centred over the wordmark; wordmark width = 1.6× the mark's width; gap = 1.5 modules.

**Wordmark.** `Casabe`, capital C, **Familjen Grotesk 700**, −0.02em tracking, **vectorised** — the lockup files contain paths, never live text. If the typeface changes (see `casabe-wordmark-fonts.html`), regenerate the lockups; the mark and the rules don't change.

## Clear space & minimum size

- **Clear space:** one module (12 units, i.e. 12% of the mark's width) on all sides, measured from the block and bar edges — not from the counter.
- **Minimum size, mark alone:** 18px tall. Below that the counter closes. The 16px favicon is the exception and works because the bar is orange and the triangle is still 4–5px.
- **Minimum size, horizontal lockup:** 30px total height, which puts the cap height at ~24px and the mark's bar still 2px clear of the block.

## Colour

Tokens from `site/styles.css`. Primary `#ff7900` is theme-invariant.

| Context | Block | Bar | Counter |
|---|---|---|---|
| Light surface, mono | ink `#16161a` | ink | shows surface |
| Light surface, two-tone (**default lockup**) | ink | `#ff7900` | shows surface |
| Dark surface (`#16161a`) | `rgba(255,255,255,.88)` | `#ff7900` | shows surface |
| Orange surface | ink | ink | shows surface |

Never set the block orange on a light surface below ~48px (contrast). The bar may be orange at any size.

For CSS-driven colour, use the `-currentcolor` files: the block and wordmark take `currentColor`, the bar is fixed orange in the `-twotone` variant.

## App icons

1024 grid, mark scaled to 64% of the canvas, centred. Three surfaces:

- **ink** — ink background, white block, orange bar *(primary app icon)*
- **orange** — orange background, ink block, ink bar
- **light** — white background, ink block, orange bar

Rounded (`rx 224`, ≈ iOS ratio) SVG/PNG for web use; `-square` files for platforms that apply their own mask (iOS, Android adaptive).

## Files — `casabe-partido-assets/`

```
Mark
  casabe-mark.svg                      ink mono
  casabe-mark-twotone.svg              ink + orange bar          ← default
  casabe-mark-inverse.svg              on-inverse mono
  casabe-mark-inverse-twotone.svg      on-inverse + orange bar
  casabe-mark-currentcolor.svg         CSS-driven, mono
  casabe-mark-currentcolor-twotone.svg CSS-driven, orange bar
  casabe-mark-{256,512,1024}.png, casabe-mark-twotone-{256,512,1024}.png

Wordmark
  casabe-wordmark.svg, casabe-wordmark-currentcolor.svg   (Familjen Grotesk 700, vectorised)

Lockups
  casabe-lockup.svg / -twotone / -inverse / -inverse-twotone / -currentcolor
  casabe-lockup-stacked.svg / -twotone / -inverse
  casabe-lockup-{800,1600}.png, casabe-lockup-twotone-{800,1600}.png

App icons
  casabe-icon-{ink,orange,light}.svg + -{1024,512,192,180,120}.png
  casabe-icon-{ink,orange}-square.svg + -square-1024.png

Favicon
  casabe-favicon.svg        (auto dark-mode via prefers-color-scheme)
  favicon-{16,32,48,64}.png
```

## Implementation notes

- `<head>`: `<link rel="icon" href="/casabe-favicon.svg" type="image/svg+xml">` with `favicon-32.png` as fallback; `apple-touch-icon` → `casabe-icon-ink-180.png`.
- Nav: `casabe-lockup-currentcolor.svg` inline, height 28–32px, colour from the nav's text token — it flips correctly on the dark band with no second file.
- The Webflow site uses Inter for UI; the lockup carries its own vectorised Familjen Grotesk wordmark, so the display face never needs to load on the site.

## Open items

- Wordmark typeface: **Familjen Grotesk 700** (provisional — may change). Comparison board: `casabe-wordmark-fonts.html`. Changing it is a regenerate of the wordmark and lockup files only.
- Dots: none in the locked version. The lab supports them if the seed idea returns.
- Update `CASABE-BRAND-GUIDELINES.md` logo section from this spec once the typeface is settled.
