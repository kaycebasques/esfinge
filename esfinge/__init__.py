import os

__version__ = '0.0.2'
__version_info__ = (0, 0, 2)

def setup(app):
    path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('esfinge', path)
