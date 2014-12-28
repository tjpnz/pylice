import unittest

from pylice.pylice import *


class TestLicenseInfo(unittest.TestCase):

    def test_get_license_info_for_distribution(self):
        self.assertRaises(Exception, get_license_info_for_distribution, "TEST")

        name, _license = get_license_info_for_distribution("setuptools")
        self.assertTrue(name.startswith("setuptools"))
        self.assertEqual(_license, "PSF or ZPL")  # Too optimistic?

    def test_get_license_info_for_working_set(self):
        license_info = get_license_info_for_working_set()
        self.assertGreater(len(license_info), 0)