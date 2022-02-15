# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.

import datetime
import mantid_sphinx_theme  # noqa: F401

# -- Project information -----------------------------------------------------
project = 'MantidProject landing page'
copyright = (
    f"2007-{datetime.datetime.now().year} ISIS Rutherford Appleton Laboratory UKRI, "
    "NScD Oak Ridge National Laboratory, European Spallation Source, "
    "Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS")

# -- General configuration ---------------------------------------------------

extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# Use our custom mantid Sphinx theme.
html_theme = "mantid_sphinx_theme"

# Path to static assets to copy to final build
html_static_path = ["_static"]

# Additional css files to include in the pages
html_css_files = ["css/landing.css"]

# Turn the left bar into news reel
html_sidebars = {
    "index": [
        "sidebar-news.html",
        "sidebar-nav-bs.html",
    ],
}
