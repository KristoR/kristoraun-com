import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F403

SITEURL = os.environ.get("SITEURL", "").rstrip("/") or "https://kristoraun.com"
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_RSS = "blog.xml"
