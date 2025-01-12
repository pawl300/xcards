# conf.py

import os
import sys
from datetime import datetime

# Add the project directory to sys.path
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'Your Project Name'
author = 'Your Name'
release = '0.1.0'  # Version of your project
year = datetime.now().year

# General configuration
extensions = [
    'sphinx.ext.autodoc',  # Automatically document Python modules
    'sphinx.ext.viewcode',  # Add links to the source code
    'sphinx.ext.githubpages',  # Support for GitHub Pages
    'sphinx.ext.napoleon',  # Support for Google and NumPy style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output options
html_theme = 'alabaster'  # You can change this to any theme you prefer
html_static_path = ['_static']

# HTML theme options
html_theme_options = {
    'description': 'A brief description of your project',
    'github_user': 'your_github_username',
    'github_repo': 'your_github_repo',
}

# Options for autodoc
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'special-members': '__init__',
}

# Options for Napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = True
