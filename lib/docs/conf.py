# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from importlib.metadata import version

sys.path.insert(0, os.path.abspath(".."))

# Mock imports (things that can't be installed at do building time)

autodoc_mock_imports = ["numpy", "pandas", "pyyaml"]

# -- Project information -----------------------------------------------------

project = "PGFinder"
copyright = "2022, PGFinder authors"
author = "PGFinder authors"

# The short X.Y version
release = version("pgfinder")
version = ".".join(release.split(".")[:2])


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx_rtd_theme",
    "myst_parser",
    "numpydoc",
    "sphinx_markdown_tables",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.jquery",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = {".rst": "restructuredtext", ".txt": "restructuredtext", ".md": "markdown"}

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "setup.py"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
# html_theme = "haiku"
# html_theme = "renku"
# html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "analytics_anonymize_ip": False,
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    # 'style_nav_header_background': '',
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
templates_path = [
    "_templates",
]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "PGFinderdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "PGFinder.tex", "PGFinder Documentation", [author], "manual"),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "PGFinder", "PGFinder Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "PGFinder", "PGFinder Documentation", author, "PGFinder", "Peptidoglycan Finder.", "Miscellaneous"),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------
# sphinx-autoapi https://sphinx-autoapi.readthedocs.io/en/latest/
autoapi_dirs = ["../pgfinder"]

# sphinx-multiversion https://holzhaus.github.io/sphinx-multiversion/master/configuration.html
smv_tag_whitelist = r"^v\d+.*$"  # Tags begining with v#
smv_branch_whitelist = r"^master$"  # main branch
# If testing changes locally comment out the above and the smv_branch_whitelist below instead. Replace the branch name
# you are working on ("ns-rse/466-doc-versions" in the example below) with the branch you are working on and run...
#
# cd docs
# sphinx-multiversion . _build/html
#
# smv_branch_whitelist = r"^(main|ns-rse/466-doc-versions)$"  # main branch
smv_released_pattern = r"^tags/.*$"  # Tags only
# smv_released_pattern = r"^(/.*)|(main).*$"  # Tags and HEAD of main
smv_outputdir_format = "{ref.name}"
