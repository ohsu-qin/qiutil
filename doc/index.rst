.. _index:

=======================================
qiutil - Quantitative Imaging Utilities
=======================================

********
Synopsis
********
qiutil provides general-purpose utilities for the `OHSU QIN`_ projects.

:API: http://qiutil.readthedocs.org/en/latest/api/index.html

:Git: https://www.github.com/ohsu-qin/qiutil


************
Feature List
************
1. Configuration file parser.

2. Logging configuration.

3. Command logging options.

4. Collection data structures and utilities. 

5. File helper functions.

6. Simple UID generator.


************
Installation
************
Add ``qiutil`` to your Python_ project setup.py ``install_requires``.


***********
Development
***********

Testing is performed with the nose_ package, which must be installed separately.

Documentation is built automatically by ReadTheDocs_ when the project is pushed
to GitHub. Documentation can be generated locally as follows:

* Install Sphinx_, if necessary.

* Run the following in the ``doc`` subdirectory::

      make html

---------

.. container:: copyright

  Copyright (C) 2014 Oregon Health & Science University `Knight Cancer Institute`_.
  See the license_ for permissions.


.. Targets:

.. _Knight Cancer Institute: http://www.ohsu.edu/xd/health/services/cancer

.. _license: https://github.com/ohsu-qin/qiutil/blob/master/LICENSE.txt

.. _nose: https://nose.readthedocs.org/en/latest/

.. _Python: http://www.python.org

.. _OHSU QIN: https://github.com/ohsu-qin

.. _ReadTheDocs: https://www.readthedocs.org

.. _Sphinx: http://sphinx-doc.org/index.html

.. toctree::
  :hidden:

  api/index
