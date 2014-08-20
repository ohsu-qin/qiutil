"""Command helper functions."""

import os
import tempfile
import logging
from . import logging_helper


def add_standard_options(parser):
    """
    Adds the :meth:`add_log_options`, ``--project`` and ``--config``
    options to the given command line arugment parser.
    """
    # The log options.
    add_log_options(parser)
    
    # The XNAT project.
    parser.add_argument('-p', '--project',
                        help="the XNAT project (default is 'QIN')")
    
    # The XNAT configuration.
    parser.add_argument('-c', '--config', help='the XNAT configuration file',
                        metavar='FILE')


def add_log_options(parser):
    """
    Adds the standard ``--log``, ``--quiet``, ``--verbose`` and ``--debug``
    options to the given command line arugment parser.
    """
    parser.add_argument('-l', '--log', help='the log file', metavar='FILE')
    verbosity_grp = parser.add_mutually_exclusive_group()
    verbosity_grp.add_argument(
        '-q', '--quiet', help="only log error messages", dest='log_level',
        action='store_const', const=logging.ERROR)
    verbosity_grp.add_argument(
        '-d', '--debug', help='log debug messages', dest='log_level',
        action='store_const', const=logging.DEBUG)


def configure_log(opts):
    """
    Configures the logger.

    :param opts: the following keyword options:
    :keyword log: the log file
    :keyword log_level: the log level
    """
    log_cfg = {}
    if 'log' in opts:
        log_file = os.path.abspath(opts.get('log'))
        log_cfg['filename'] = log_file
    if 'log_level' in opts:
        log_cfg['level'] = opts.get('log_level')
    logging_helper.configure(**log_cfg)
