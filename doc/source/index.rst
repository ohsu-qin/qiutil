.. _index:

=======================================
qiutil - Quantitative Imaging Utilities
=======================================

********
Synopsis
********
qiutil provides helper modules for processing images.

:API: http://quip1.ohsu.edu:8080/qiutil/api

:Git: git\@quip1.ohsu.edu:qiutil
      (`Browse <http://quip1.ohsu.edu:6060/qiutil>`__)


************
Feature List
************
1. XNAT_ facade API.

2. XNAT list, transfer and delete.

3. DICOM metadata list and edit.

4. Python logging configuration.


************
Installation
************
1. Install Git_ on your workstation, if necessary.

2. Contact the qiutil `OHSU QIN Git administrator`_ to get permission to
   access the qiutil Git repository.

3. Clone the `qiutil repository`_::

       cd ~/workspace
       git clone git@quip1:qiutil
       cd qiutil

4. Activate an Anaconda_ virtual environment, e.g.::

       source activate qipipe

5. On Linux only, install the ``libxslt`` dev package. For Ubuntu or other
   Debian-based systems, use::

       sudo aptitude install libxslt-dev

   For Red Hat, use::
   
       sudo yum install libxslt-dev

6. On Mac only, install the ``lxml`` Python package with statically bound
   libraries::

       (STATIC_DEPS=true; pip install lxml)

7. Install the Anaconda packages::

       for p in `cat requirements.txt`; do conda install $p; done 

7. Install the remaining packages using pip_::

       pip install -r requirements.txt

8. Finally, install the ``qiutil`` package::

       pip install -e .


*****
Usage
*****
Run the following command for the utility options::

    lsdicom --help
    qicp --help
    qils --help
    qirm --help

---------

.. container:: copyright

  Copyright (C) 2014 Oregon Health & Science University
  `Knight Cancer Institute`_. All rights reserved. ``qiutil`` is confidential
  and may not be distributed in any form without authorization.


.. Targets:

.. _Anaconda: http://docs.continuum.io/anaconda/

.. _Git: http://git-scm.com

.. _Knight Cancer Institute: http://www.ohsu.edu/xd/health/services/cancer

.. _OHSU QIN Git administrator: loneyf@ohsu.edu

.. _pip: https://pypi.python.org/pypi/pip

.. _Python: http://www.python.org

.. _qiutil repository: http://quip1.ohsu.edu:6060/qiutil

.. _XNAT: http://www.xnat.org/

.. toctree::
  :hidden:

  api/index
