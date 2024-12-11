# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# These four objects provided with initial setup
project = "CMAQ"
copyright = '2023, CMAQ Developers'
author = 'CMAQ Developers'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# These three objects provided with initial setup - 'myst_parser' added later
extensions = [
        'myst_parser',
#        'sphinx.ext.autodoc',
        'sphinx.ext.autosectionlabel',
        'sphinx.ext.napoleon',
        'sphinx.ext.viewcode',
        'sphinx.ext.imgconverter',
#        'sphinx.ext.githubpages',
#        'sphinx_gallery.gen_gallery',
#        'sphinx_panels'
        'sphinx_design',
        'sphinx_copybutton'
]
myst_enable_extensions = ["colon_fence", "linkify"]
myst_heading_anchors = 1

templates_path = ['_templates']
exclude_patterns = []

# custom provides configuration values
source_suffix = {
        '.rst': 'restructuredtext',
        '.txt': 'restructuredtext',
        '.md': 'markdown',
}

import pydata_sphinx_theme
html_theme = 'alabaster'
html_static_path = ['_static']
html_sidebars = {
        'index': ['searchbox.html'],
        '**': ['searchbox.html']
        }

html_theme_options = {
    "github_url": "https://github.com/USEPA/CMAQ",
    "logo": {
        "image_light": "_static/CMAQ_Logo_2_inch.png",
        "image_dark": "_static/CMAQ_Logo_2_inch.png",
    }
}
