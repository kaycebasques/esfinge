import os

__version__ = '0.0.5'
__version_info__ = (0, 0, 5)

def setup(app):
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('esfinge', theme_path)
    return {'version': __version__, 'parallel_read_safe': True}
