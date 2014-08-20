import os
import shutil
from nose.tools import (assert_equal, assert_true)
from qiutil import logging_helper
from qiutil.logging_helper import logger

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
"""The test parent directory."""

FIXTURE = os.path.join(ROOT, 'fixtures', 'helpers', 'logging', 'logging.yaml')
"""The test fixture logging configuration file."""

RESULTS = os.path.join(ROOT, 'results', 'helpers', 'logging')
"""The test result parent directory."""

RESULT = os.path.join(RESULTS, 'log', 'qiutil.log')
"""The resulting test log."""


class TestLoggingHelper(object):

    """The logging unit tests."""

    def setUp(self):
        shutil.rmtree(RESULTS, True)

    def tearDown(self):
        shutil.rmtree(RESULTS, True)

    def test_filename(self):
        logging_helper.configure(filename=RESULT)
        logger('qiutil').info("Test info log message.")
        logger('qiutil').debug("Test debug log message.")
        assert_true(os.path.exists(RESULT),
                    "The log file was not created: %s" % RESULT)
        with open(RESULT) as fs:
            msgs = fs.readlines()
        assert_true(not not msgs, "No log messages in %s" % RESULT)
        assert_equal(len(msgs), 1, "Extraneous log messages in %s" % RESULT)

    def test_level(self):
        logging_helper.configure(filename=RESULT, level='DEBUG')
        logger('qiutil').info("Test info log message.")
        logger('qiutil').debug("Test debug log message.")
        assert_true(os.path.exists(RESULT),
                    "The log file was not created: %s" % RESULT)
        with open(RESULT) as fs:
            msgs = fs.readlines()
        assert_true(not not msgs, "No log messages in %s" % RESULT)
        assert_equal(len(msgs), 2, "Extraneous log messages in %s" % RESULT)

if __name__ == "__main__":
    import nose

    nose.main(defaultTest=__name__)
