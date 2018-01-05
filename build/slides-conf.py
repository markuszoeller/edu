# -*- coding: utf-8 -*-

# -- General configuration ------------------------------------------------
extensions = ['hieroglyph']

templates_path = ['_templates']
exclude_patterns = ['_build']
source_suffix = '.rst'

master_doc = 'index'

project = u'Slides'
copyright = u'2017, Markus Zoeller'
author = u'Markus Zoeller'
# TODO: Use ``git describe`` here.
version = u'2017.12.28'
release = version  # it's always the same
language = "en"

pygments_style = 'sphinx'
todo_include_todos = True

# -- hieroglyph options ------------------------------------------------------
slide_theme = "single-level" # slides, slides2, single-level
