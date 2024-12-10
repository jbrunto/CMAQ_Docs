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
extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

# custom provides configuration values
source_suffix = {
        '.rst': 'restructuredtext',
        '.txt': 'restructuredtext',
        '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# These two objects provided with initial setup
import pydata_sphinx_theme
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_show_sourcelink = True
html_sidebars = {
        '**': ['localtoc.html', 'sourcelink.html']
        }


html_theme_options = {
    "github_url": "https://github.com/USEPA/CMAQ",
    "logo": {
        "image_light": "_static/CMAQ_Logo_2_inch.png",
        "image_dark": "_static/CMAQ_Logo_2_inch.png",
    }





 }
