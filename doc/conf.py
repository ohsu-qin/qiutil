import os
import qiutil

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo']
autoclass_content = "both"
autodoc_default_flags= ['members', 'show-inheritance']
source_suffix = '.rst'
master_doc = 'index'
project = u'qiutil'
copyright = u'2014, OHSU Knight Cancer Institute. This software is not intended for clinical use'
version = qiutil.__version__
pygments_style = 'sphinx'
html_title = "qiutil v%s" % version


def skip(app, what, name, obj, skip, options):
    """
    @return False if the name is __init__ or *skip* is set, True otherwise
    """
    return skip and name is not "__init__"


def setup(app):
    """
    Directs autodoc to call :meth:`skip` to determine whether to skip a member.
    """
    app.connect("autodoc-skip-member", skip)
