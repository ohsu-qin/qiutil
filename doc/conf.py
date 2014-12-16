import os
import qiutil

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo']
autoclass_content = "both"
templates_path = ['templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'qiutil'
copyright = u'2014, OHSU Knight Cancer Institute'
version = qiutil.__version__
pygments_style = 'sphinx'
#html_theme = 'theme'
#html_theme_path = ['.']
#html_theme_options = dict(linkcolor='DarkSkyBlue', visitedlinkcolor='Navy')
#htmlhelp_basename = 'qiutildoc'
html_title = "qiutil v%s" % version
