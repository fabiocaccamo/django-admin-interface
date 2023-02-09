import re

from django.test import TestCase

from admin_interface.metadata import (
    __author__,
    __copyright__,
    __description__,
    __email__,
    __license__,
    __title__,
    __version__,
)


class MetadataTestCase(TestCase):
    """
    This class describes a metadata test case.
    """

    def test_metadata(self):
        self.assertTrue(isinstance(__author__, str))
        self.assertTrue(isinstance(__copyright__, str))
        self.assertTrue(isinstance(__description__, str))
        self.assertTrue(isinstance(__email__, str))
        self.assertTrue(isinstance(__license__, str))
        self.assertTrue(isinstance(__title__, str))
        self.assertTrue(isinstance(__version__, str))

    def test_version(self):
        v = __version__
        v_re = re.compile(r"^([0-9]+)(\.([0-9]+)){1,2}$")
        v_match = v_re.match(v)
        self.assertTrue(v_match is not None)
