"""
This plugin searches for Sqreen tokens.
"""
from __future__ import absolute_import

import re

from .base import RegexBasedDetector


class SqreenTokenDetector(RegexBasedDetector):
    """Scans for Sqreen tokens."""
    secret_type = 'Sqreen tokens'

    denylist = [
        # Org token (org_...)
        re.compile(r'org_.*'),
    ]
