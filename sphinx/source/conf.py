# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# These four objects provided with initial setup
project = "CMAQ Critical Documentation"
copyright = '2023, JBrunton'
author = 'JBrunton'
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
html_theme = 'classic'
html_static_path = ['_static']
