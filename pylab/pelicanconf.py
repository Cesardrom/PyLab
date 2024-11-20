AUTHOR = 'Cesar Dominguez, Jose Rodriguez, Nichole Louis'
SITENAME = 'PyLab'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Servicios', '/nuestros-servicios.html'),
    ('Contacto', '/contactanos.html'),
    ('Inicio', '/index.html'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = './themes/pelican-chunk-f9206df831d497688516cf86dd089004be1ee06a'
# Para los html
STATIC_PATHS = ['images']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Para los post _/blog
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

# Categorias
CATEGORY_URL = 'categoria/{slug}/'
CATEGORY_SAVE_AS = 'categoria/{slug}/index.html'

# Tags

TAG_URL = 'etiqueta/{slug}/'
TAG_SAVE_AS = 'etiqueta/{slug}/index.html'
