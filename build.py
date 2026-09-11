"""Build the canvas pouch workshop page.

    python3 build.py

Inlines the Casabe marketing-site stylesheet and the two brand fonts into
src/body.html, so the page fetches nothing, and writes:

  canvas-pouch/index.html  the public page, https://workshops.casabe.studio/canvas-pouch/
  index.html               redirect from the bare address to the page
  artifact.html            the page without <head>, for the claude.ai artifact copy

Brand sources are read from the sibling checkouts in ~/Git Library.
"""
import re, pathlib

LIB = pathlib.Path(__file__).resolve().parent.parent
here = pathlib.Path(__file__).resolve().parent

fonts = "\n".join(re.findall(
    r"@font-face\s*\{.*?\}",
    (LIB / "design-system-library/systems/house-default/dist/components.css").read_text(),
    flags=re.S))
site = (LIB / "batey-platform/site/styles.css").read_text()
# Let an explicit host "light" beat a dark OS, same as the site's .theme-light escape hatch.
site = site.replace("html:not(.theme-light) {", 'html:not(.theme-light):not([data-theme="light"]) {')

body = (here / "src/body.html").read_text()

# Step diagrams: shared styles/defs go in above the nav; each figure goes into
# its step, just above the Done button.
diagrams = (here / "src/diagrams.html").read_text()
shared, _, _ = diagrams.partition('<figure class="step-fig"')
body = body.replace('<header class="main-nav">', shared.strip() + '\n\n<header class="main-nav">', 1)
for fig in re.findall(r'<figure class="step-fig" data-step="\d+">.*?</figure>', diagrams, flags=re.S):
    n = re.search(r'data-step="(\d+)"', fig).group(1)
    done = '<label class="step-done"><input class="checkbox" type="checkbox" data-track="step-%s">' % n
    assert body.count(done) == 1, "no single Done button for step " + n
    body = body.replace(done, fig + "\n          " + done)

page = body.replace("<!--SITE_CSS-->", "<style>\n" + fonts + "\n" + site + "\n</style>")
(here / "artifact.html").write_text(page)

title = re.search(r"<title>.*?</title>", page).group(0)
(here / "canvas-pouch").mkdir(exist_ok=True)
(here / "canvas-pouch/index.html").write_text(
    '<!doctype html>\n<html lang="en" data-direction="bold">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="Handout for the canvas zip pouch workshop: materials, colors and step-by-step instructions with diagrams.">\n'
    '<meta name="robots" content="noindex">\n'
    + title + "\n</head>\n<body>\n"
    + page.replace(title, "", 1)
    + "\n</body>\n</html>\n")

# The bare workshops.casabe.studio address has no page of its own yet; send
# people to the one workshop there is.
(here / "index.html").write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    '<meta name="robots" content="noindex">\n'
    '<meta http-equiv="refresh" content="0; url=canvas-pouch/">\n'
    '<title>Casabe Workshops</title>\n'
    '</head>\n<body>\n'
    '<p><a href="canvas-pouch/">Canvas zip pouch workshop</a></p>\n'
    '</body>\n</html>\n')
print("canvas-pouch/index.html", (here / "canvas-pouch/index.html").stat().st_size, "bytes")
