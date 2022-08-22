"""Sphinx configuration."""
project = "EyeLink Parser"
author = "Maciej Skórski"
copyright = "2022, Maciej Skórski"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
