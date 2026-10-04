# kristoraun.com

My personal site, built with [Pelican](https://getpelican.com) from Markdown.
Hand-written templates, one stylesheet, no JavaScript.

## Running locally

```
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pelican --autoreload --listen
```

The site is then at http://localhost:8000.

## Writing

Posts go in `content/blog/` and projects in `content/projects/`, one Markdown
file each. The file name becomes the URL.

```
Title: A clear title
Date: 2026-11-01
Summary: One sentence for listings and link previews.

The post itself, in Markdown.
```

Photos go through `optimize_images.py`, which resizes them, converts them to
WebP and prints the HTML to paste into the post:

```
.venv/bin/python optimize_images.py photo.jpg "Caption"
```
