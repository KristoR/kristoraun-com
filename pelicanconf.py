AUTHOR = "Kristo Raun"
SITENAME = "Kristo Raun"
SITEURL = ""
RELATIVE_URLS = False

PATH = "content"
THEME = "theme"
TIMEZONE = "Europe/Tallinn"
DEFAULT_LANG = "en"

PROFILE = {
    "name": "Kristo Raun",
    "job_title": "Data Engineer",
    "works_for": "Lightyear",
    "description": (
        "Data engineer at Lightyear, working across data engineering, "
        "analytics, data strategy, and governance."
    ),
    "linkedin": "https://www.linkedin.com/in/kristoraun/",
    "knows_about": [
        "Data engineering",
        "Analytics",
        "Data strategy",
        "Data governance",
        "Data platforms",
        "Streaming conformance checking",
    ],
}

ARTICLE_PATHS = ["blog", "projects"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["images"]
PATH_METADATA = r"(?P<category>blog|projects)/.*"
# Hidden articles stay out of feeds, which keeps RSS blog-only.
EXTRA_PATH_METADATA = {"projects": {"status": "hidden"}}
SLUGIFY_SOURCE = "basename"

ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

DIRECT_TEMPLATES = ["blog", "projects"]
BLOG_SAVE_AS = "blog/index.html"
PROJECTS_SAVE_AS = "projects/index.html"
DEFAULT_PAGINATION = False

TAG_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
DRAFT_SAVE_AS = ""
DRAFT_PAGE_SAVE_AS = ""

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

DELETE_OUTPUT_DIRECTORY = True
