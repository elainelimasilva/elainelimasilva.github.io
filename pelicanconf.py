# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

# THINGS TO CONFIGURE
# ---------------------------------------------------------------------

AUTHOR = "Elaine Lima"
AUTHORS = {
    "Elaine Lima": {
        "blurb": "descrição de autora aqui",
        "url": "https://elainelimasilva.github.io",
        "avatar": "https://avatars.githubusercontent.com/u/77029826",
    },
}
SITENAME = "Blog da Professora Elaine Lima"
SITESUBTITLE = "Subtitulo de rodapé aqui"
SITEDESCRIPTION = "Blog pessoal da Professora Elaine Lima sobre Sociologia"
SITEURL = "http://127.0.0.1:8000"
DEFAULT_LANG = "pt"
DEFAULT_CATEGORY = "blog"
CLAIM_GOOGLE = "hPsjXvZJKWUu9ml7OJHienwqSordoOb5oZ8jJ3pFYco"
CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"


LANDING_PAGE_TITLE = "Não somos, intersomos"

PROJECTS_TITLE = "Projetos"
PROJECTS = [
    {
        "name": "Canal da Professora Elaine",
        "url": "https://www.youtube.com/channel/UC6b7RrF8m7hMuNnbwmyLtKw",
        "description": "Meu canal no Youtube",
    },
    {
        "name": "Narrativas Femininas",
        "url": "https://instagram.com/narrativa_femininas",
        "description": "Experiências e conteudos sobre maternidade, envelhecimento, empoderamento e identidades",
    },
]

LINKS = (
    ("Redken on telegram", "https://t.me/redken_bot"),
    ("RHJobs channel on TG", "https://t.me/rhjobs"),
)

# Keep 'name' like 'twitter' with what 'FontAwesome has for putting the right icon'

SOCIAL = (
    ("gmail", "mailto:narrativasfemininas@gmail.com"),
    ("youtube", "https://www.youtube.com/channel/UC6b7RrF8m7hMuNnbwmyLtKw"),
    ("instagram", "https://instagram.com/elaine.lima.silva"),
    ("facebook", "https://facebook.com/elaine.limadasilva"),
    ("twitter", "https://twitter.com/ElaineLimadaSi8"),
)


TWITTER_USERNAME = "ElaineLimadaSi8"
# Update if you use amazon links
# AMAZON_ONELINK = "23824450-ef77-4537-9259-8590465886f1"

# GOOGLE_ANALYTICS tracking ID
# GOOGLE_ANALYTICS = "UA-81705-12"

# Configure if you use Disqus for comments
DISQUS_SITENAME = "elainelimasilva-github-io"
DISQUS_DISPLAY_COUNTS = True


# Extra files customization
EXTRA_PATH_METADATA = {}

EXTRA_TEMPLATES_PATHS = [
    "plugins/revealmd/templates",  # eg: "plugins/revealmd/templates"
]

STATIC_PATHS = ["images"]

# Photo Gallery plugin
PHOTO_LIBRARY = "gallery-source/"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = ""  # © Elaine Lima"
PHOTO_WATERMARK_IMG = ""
PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True
PHOTO_EXIF_COPYRIGHT = "COPYRIGHT"
# PHOTO_EXIF_COPYRIGHT_AUTHOR = 'Your Name Here' (Defaults to Author)

# ONLY TOUCH IF YOU KNOW WHAT YOU'RE DOING!
# ---------------------------------------------------------------------

PATH = "content"

TIMEZONE = "America/Sao_Paulo"
DATE_FORMATS = {"pt": "%b %d, %Y"}

READING_TIME_LOWER_LIMIT = 3


# Put as draft content in the future
WITH_FUTURE_DATES = True

# Put full text in RSS feed
RSS_FEED_SUMMARY_ONLY = False

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss"

CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss"
TRANSLATION_FEED_ATOM = "feeds/{lang}.atom.xml"
TRANSLATION_FEED_RSS = "feeds/{lang}.rss"
AUTHOR_FEED_ATOM = "feeds/{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/{slug}.rss"
TAG_FEED_ATOM = "feeds/tag_{slug}.atom.xml"
TAG_FEED_RSS = "feeds/tag_{slug}.rss"

DISPLAY_PAGES_ON_MENU = True

CACHE_CONTENT = False
CACHE_PATH = ".cache"
LOAD_CONTENT_CACHE = False

# Plugins
PLUGIN_PATHS = ["plugins"]

PLUGINS = [
    "sitemap",
    "extract_toc",
    "tipue_search",
    "liquid_tags.img",
    "neighbors",
    "render_math",
    "related_posts",
    "share_post",
    "series",
    "assets",
    "post_stats",
    "revealmd",
    "photos",
]

# 'better_codeblock_line_numbering'
# 'better_figures_and_images'

THEME = "themes/elegant"

# elegant
TYPOGRIFY = True
RECENT_ARTICLE_SUMMARY = False
RESPONSIVE_IMAGES = True

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight", "linenums": True},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"permalink": "true"},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Mantenha contato"
RELATED_POSTS_LABEL = "Leia mais"
SHARE_POST_INTRO = "Gostou desta publicação? Compartilhe:"
COMMENTS_INTRO = ""

FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"
USE_FOLDER_AS_CATEGORY = False

SEARCH_BOX = False

# URL Settings to be compatible with octopress
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

ARTICLE_LANG_URL = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/"
ARTICLE_LANG_SAVE_AS = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html"

YEAR_ARCHIVE_URL = "blog/archive/{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "blog/archive/{date:%Y}/index.html"

MONTH_ARCHIVE_URL = "blog/archive/{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "blog/archive/{date:%Y}/{date:%m}/index.html"

CATEGORY_URL = "blog/category/{slug}/"
CATEGORY_SAVE_AS = "blog/category/{slug}/index.html"

TAG_URL = "blog/tag/{slug}/"
TAG_SAVE_AS = "blog/tag/{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

ARCHIVES_URL = "blog/archives/"
ARCHIVES_SAVE_AS = "blog/archives/index.html"

CATEGORIES_URL = "blog/categories/"
CATEGORIES_SAVE_AS = "blog/categories/index.html"

TAGS_URL = "blog/tags/"
TAGS_SAVE_AS = "blog/tags/index.html"

TAGS_URL = "tags"
TAGS_SAVE_AS = "tags/index.html"
AUTHORS_URL = "authors"
AUTHORS_SAVE_AS = "authors/index.html"
CATEGORIES_URL = "categories"
CATEGORIES_SAVE_AS = "categories/index.html"
ARCHIVES_URL = "archives"
ARCHIVES_SAVE_AS = "archives/index.html"

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 0

PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

SITE_UPDATED = datetime.date.today()

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ("Tags", TAGS_URL, TAGS_SAVE_AS),
    ("Archives", ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
