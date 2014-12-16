import os
import qiutil

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo']
autoclass_content = "both"
source_suffix = '.rst'
master_doc = 'index'
project = u'qiutil'
copyright = u'2014, OHSU Knight Cancer Institute'
version = qiutil.__version__
pygments_style = 'sphinx'
html_title = "qiutil v%s" % version
