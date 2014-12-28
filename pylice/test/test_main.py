import StringIO
import csv
import unittest

from pylice.main import get_license_info


class TestMain(unittest.TestCase):

    def test_get_all_licenses(self):
        output = get_license_info()
        self.assertGreater(len(output), 0)

    def test_get_license_for_package(self):
        output = get_license_info(packages=["setuptools"])
        self.assertTrue(output.startswith("setuptools"))
        self.assertTrue(output.strip().endswith("PSF or ZPL"))

    def test_csv_output(self):
        output = get_license_info(output_csv=True)
        csv_reader = csv.reader(StringIO.StringIO(output))
        for row in csv_reader:
            self.assertEqual(len(row), 2)