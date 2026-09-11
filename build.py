"""Build the canvas pouch workshop pages.

    python3 build.py

Inlines the Casabe marketing-site stylesheet and the two brand fonts, so the
pages fetch nothing but the progress API, and writes:

  canvas-pouch/index.html           the attendee page, https://workshops.casabe.studio/canvas-pouch/
  canvas-pouch/progress/index.html  the instructor's progress page (data needs the secret link's key)
  index.html                        redirect from the bare address to the attendee page
  artifact.html                     the attendee page without <head>, for the claude.ai copy

Brand sources are read from the sibling checkouts in ~/Git Library.
"""
import html, json, re, pathlib

LIB = pathlib.Path(__file__).resolve().parent.parent
here = pathlib.Path(__file__).resolve().parent

fonts = "\n".join(re.findall(
    r"@font-face\s*\{.*?\}",
    (LIB / "design-system-library/systems/house-default/dist/components.css").read_text(),
    flags=re.S))
site = (LIB / "batey-platform/site/styles.css").read_text()
# Let an explicit host "light" beat a dark OS, same as the site's .theme-light escape hatch.
site = site.replace("html:not(.theme-light) {", 'html:not(.theme-light):not([data-theme="light"]) {')
site_css = "<style>\n" + fonts + "\n" + site + "\n</style>"


def full_page(page, description):
    title = re.search(r"<title>.*?</title>", page).group(0)
    return ('<!doctype html>\n<html lang="en" data-direction="bold">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<meta name="description" content="' + description + '">\n'
            '<meta name="robots" content="noindex">\n'
            + title + "\n</head>\n<body>\n"
            + page.replace(title, "", 1)
            + "\n</body>\n</html>\n")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print(path.relative_to(here), path.stat().st_size, "bytes")


# ---- attendee page ----
body = (here / "src/body.html").read_text()

# Step diagrams: shared styles/defs go in above the nav; each figure goes into
# its step, just above the Done button.
diagrams = (here / "src/diagrams.html").read_text()
shared, _, _ = diagrams.partition('<figure class="step-fig"')
page = body.replace('<header class="main-nav">', shared.strip() + '\n\n<header class="main-nav">', 1)
for fig in re.findall(r'<figure class="step-fig" data-step="\d+">.*?</figure>', diagrams, flags=re.S):
    n = re.search(r'data-step="(\d+)"', fig).group(1)
    done = '<label class="step-done"><input class="checkbox" type="checkbox" data-track="step-%s">' % n
    assert page.count(done) == 1, "no single Done button for step " + n
    page = page.replace(done, fig + "\n          " + done)

page = page.replace("<!--SITE_CSS-->", site_css)
write(here / "artifact.html", page)
write(here / "canvas-pouch/index.html", full_page(
    page, "Handout for the canvas zip pouch workshop: materials, colors and step-by-step instructions with diagrams."))

# ---- instructor progress page ----
# Stage and step names come from the attendee page, so the two never disagree.
stages = []
for m in re.finditer(r'<div class="phase" id="[^"]+">\s*<h3 class="phase_title">(.*?) <span', body):
    end = body.find('<div class="phase"', m.end())
    chunk = body[m.end(): end if end != -1 else len(body)]
    steps = [[int(n), html.unescape(t)] for n, t in
             re.findall(r'<li class="steps_item is-timeline" id="step-(\d+)">\s*<h4 class="steps_title">(.*?)</h4>', chunk)]
    stages.append({"title": html.unescape(m.group(1)), "steps": steps})
assert sum(len(s["steps"]) for s in stages) == 19, "expected 19 steps across the stages"
stages_js = "<script>var STAGES = " + json.dumps(stages).replace("</", "<\\/") + ";</script>"

progress = (here / "src/progress.html").read_text()
progress = progress.replace("<!--SITE_CSS-->", site_css).replace("<!--STEPS_JSON-->", stages_js)
write(here / "canvas-pouch/progress/index.html", full_page(progress, "Instructor progress view for the canvas zip pouch workshop."))

# ---- bare address: send people to the one workshop there is ----
write(here / "index.html",
      '<!doctype html>\n<html lang="en">\n<head>\n'
      '<meta charset="utf-8">\n'
      '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      '<meta name="robots" content="noindex">\n'
      '<meta http-equiv="refresh" content="0; url=canvas-pouch/">\n'
      '<title>Casabe Workshops</title>\n'
      '</head>\n<body>\n'
      '<p><a href="canvas-pouch/">Canvas zip pouch workshop</a></p>\n'
      '</body>\n</html>\n')
