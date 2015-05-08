import os
import shutil
from nose.tools import (assert_equal, assert_not_equal, assert_true)
from qiutil import logging
from qiutil.logging import logger
from qiutil.cd import cd
from .. import ROOT

FIXTURE = os.path.join(ROOT, 'fixtures', 'logging', 'logging.yaml')
"""The test fixture logging configuration file."""

RESULTS = os.path.join(ROOT, 'results', 'logging')
"""The test result parent directory."""

RESULT = os.path.join(RESULTS, 'log', 'test.log')
"""The resulting test log."""


class TestLogging(object):
    """The logging unit tests."""

    def setUp(self):
        shutil.rmtree(RESULTS, True)

    def tearDown(self):
        shutil.rmtree(RESULTS, True)

    def test_log_file(self):
        logging.configure('test', filename=RESULT)
        logger('test').info("Test info log message.")
        logger('test').debug("Test debug log message.")
        assert_true(os.path.exists(RESULT),
                    "The log file was not created: %s" % RESULT)
        with open(RESULT) as fs:
            msgs = fs.readlines()
        assert_true(not not msgs, "No log messages in %s" % RESULT)
        assert_equal(len(msgs), 1, "Extraneous log messages: %s" % msgs)

    def test_level(self):
        logging.configure('test', filename=RESULT, level='DEBUG')
        logger('test').info("Test info log message.")
        logger('test').debug("Test debug log message.")
        assert_true(os.path.exists(RESULT),
                    "The log file was not created: %s" % RESULT)
        with open(RESULT) as fs:
            msgs = fs.readlines()
        assert_true(not not msgs, "No log messages in %s" % RESULT)
        assert_not_equal(len(msgs), 1, "Missing log messages in %s" % RESULT)
        assert_equal(len(msgs), 2, "Extraneous log messages in %s" % RESULT)

    def test_config_file(self):
        os.makedirs(RESULTS)
        # Since the config fixture specifies a relative log file 'log/test.log',
        # run this test in the context of the results directory.
        with cd(RESULTS):
            logging.configure('test', config=FIXTURE)
            logger('test').info("Test info log message.")
        assert_true(os.path.exists(RESULT), "The log file was not created: %s" %
                                            RESULT)
        with open(RESULT) as fs:
            msgs = fs.readlines()
            assert_true(not not msgs, "No log messages in %s" % RESULT)
            msg = msgs[0]
            assert_true(msg.startswith('Custom: '), "The log message format is"
                                                    " incorrect: %s" % msg)

if __name__ == "__main__":
    import nose

    nose.main(defaultTest=__name__)
