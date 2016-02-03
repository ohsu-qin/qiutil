import os
import tempfile
from nose.tools import (assert_equal, assert_is_not_none)
from ..helpers.logging import logger
from qiutil.ast_config import read_config
from .. import ROOT

FIXTURE = os.path.join(ROOT, 'fixtures', 'ast_config', 'tuning.cfg')
"""The test fixture configuration file."""


class TestASTConfig(object):
    """The ASTConfig unit tests."""
    
    def test_read(self):
        logger(__name__).debug("Testing the JSON configuration loader on"
                               " %s..." % FIXTURE)
        cfg = read_config(FIXTURE)
        assert_is_not_none(cfg.has_section('Tuning'),
                           "The configuration is missing the Tuning section")
        opts = cfg['Tuning']
        expected = dict(method='FFT',
                        description="String with [ ( 3 , a\" ' 4.5 'b' ) ] characters",
                        iterations=[1, [2, [3, 4], 5]],
                        parameters=[(1,), (2, 3)],
                        sampling=[0.3, [None, [None] * 2, 1.0], -0.1],
                        two_tailed=[True, False],
                        threshold=1.2e-8,
                        plugin_args=dict(
                            qsub_args='-pe mpi 48-120 -l h_rt=4:00:00,mf=2G'' -b n',
                            overwrite=True))
        
        assert_equal(opts, expected, "The configuration Tuning options are"
                     " incorrect: %s" % opts)
    
    def test_write(self):
        # The test config.
        expected_cfg = read_config(FIXTURE)
        with tempfile.NamedTemporaryFile() as copy:
            # Write out a copy.
            expected_cfg.write(copy)
            copy.flush()
            # Read the copy back in.
            actual_cfg = read_config(copy.name)
            # Compare the round-trip result.
            expected_sections = set(expected_cfg.sections())
            actual_sections = set(actual_cfg.sections())
            assert_equal(actual_sections, expected_sections,
                         "The configuration round-trip sections differ:"
                         " %s vs %s" % (actual_sections, expected_sections))
            for section in expected_sections:
                expected_content = dict(expected_cfg.items(section))
                actual_content = dict(actual_cfg.items(section))
                expected_keys = set(expected_content.keys())
                actual_keys = set(actual_content.keys())
                
                assert_equal(actual_keys, expected_keys,
                             "The configuration round-trip %s section keys"
                             " differ: %s vs %s" %
                             (section, actual_keys, expected_keys))
                for key, expected_value in expected_content.items():
                    actual_value = actual_content[key]
                    assert_equal(actual_value, expected_value,
                                 "The configuration round-trip %s section %s"
                                 " values differ: %s vs %s" %
                                 (section, key, actual_value, expected_value))


if __name__ == "__main__":
    import nose
    
    nose.main(defaultTest=__name__)
