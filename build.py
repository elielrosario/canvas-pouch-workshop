"""Build the canvas pouch workshop page.

    python3 build.py

Inlines the Casabe marketing-site stylesheet and the two brand fonts into
src/body.html, so the page fetches nothing, and writes:

  index.html     the public page (GitHub Pages serves this)
  artifact.html  the same page without <head>, for the claude.ai artifact copy

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
page = body.replace("<!--SITE_CSS-->", "<style>\n" + fonts + "\n" + site + "\n</style>")
(here / "artifact.html").write_text(page)

title = re.search(r"<title>.*?</title>", page).group(0)
(here / "index.html").write_text(
    '<!doctype html>\n<html lang="en" data-direction="bold">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="Handout for the canvas zip pouch workshop: what to bring, cutting chart and step-by-step instructions.">\n'
    '<meta name="robots" content="noindex">\n'
    + title + "\n</head>\n<body>\n"
    + page.replace(title, "", 1)
    + "\n</body>\n</html>\n")
print("index.html", (here / "index.html").stat().st_size, "bytes")
