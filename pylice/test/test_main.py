try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import csv
import unittest

from pylice import get_license_info


class TestMain(unittest.TestCase):

    def test_get_all_licenses(self):
        output = get_license_info()
        self.assertGreater(len(output), 0)

    def test_get_license_for_package(self):
        output = get_license_info(packages=["Python"])
        self.assertTrue(output.startswith("Python"))
        self.assertTrue(output.strip().endswith("PSF license"))

    def test_csv_output(self):
        output = get_license_info(output_csv=True)
        csv_reader = csv.reader(StringIO(output))
        for row in csv_reader:
            self.assertEqual(len(row), 2)