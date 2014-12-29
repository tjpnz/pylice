import unittest

from pylice import license


class TestLicense(unittest.TestCase):

    def test_get_license_info_for_distribution(self):
        self.assertRaises(Exception, license.get_license_info_for_distribution, "TEST")

        name, _license = license.get_license_info_for_distribution("setuptools")
        # Check for setuptools (Python 2) or distribute (Python 3)
        self.assertTrue(name.startswith("setuptools") or name.startswith('distribute'))
        self.assertEqual(_license, "PSF or ZPL")  # Too optimistic?

    def test_get_license_info_for_working_set(self):
        license_info = license.get_license_info_for_working_set()
        self.assertGreater(len(license_info), 0)