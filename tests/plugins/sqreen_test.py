from __future__ import absolute_import

import pytest

from detect_secrets.plugins.sqreen import SqreenTokenDetector


class TestTwilioKeyDetector(object):

    @pytest.mark.parametrize(
        'payload, should_flag',
        [
            (
                'org_512ee4512ee4512ee4512ee4512ee4512ee4512ee4512ee4512ee4512ee4',
                True,
            ),
        ],
    )
    def test_analyze(self, payload, should_flag):
        logic = SqreenTokenDetector()
        output = logic.analyze_line(payload, 1, 'mock_filename')
        assert output
