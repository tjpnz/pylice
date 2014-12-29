import unittest

from pylice import license


class TestLicense(unittest.TestCase):

    def test_get_license_info_for_distribution(self):
        self.assertRaises(Exception, license.get_license_info_for_distribution, "TEST")

        name, _license = license.get_license_info_for_distribution("Python")
        self.assertTrue(name.startswith("Python"))
        self.assertEqual(_license, "PSF license")

    def test_get_license_info_for_working_set(self):
        license_info = license.get_license_info_for_working_set()
        self.assertGreater(len(license_info), 0)