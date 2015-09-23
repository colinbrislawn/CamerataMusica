#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin Brislawn'
SITENAME = u'Camerata Musica'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
	('Facebook', 'https://www.facebook.com/pages/Camerata-Musica-Richland/226889204035616'),
	('Origional site','http:///www.cameratamusica.com'),
	('GitHub', 'https://github.com/colinbrislawn'),
	)

NEWEST_FIRST_ARCHIVES = True
DEFAULT_PAGINATION = 10
#ARTICLE_ORDER_BY = 'date'
ARTICLE_ORDER_BY = 'date'
NEWEST_FIRST_ARCHIVES = False

PAGE_ORDER_BY = 'reversed-date'
#LOAD_CONTENT_CACHE = False



STATIC_PATHS = ['images', 'pages', 'favicon.png', 'CamerataMusica/images']


SUMMARY_MAX_LENGTH = 20


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "./pelican-bootstrap3"
#THEME = "../pelican-themes/bootstrap2"
#THEME = "../pelican-themes/bootstrap2-dark"

PLUGIN_PATHS = ['../pelican-plugins']
#PLUGINS=['sitemap',]
