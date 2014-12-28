try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import argparse
import csv
import sys

try:
    from pylice.pylice import *
except ImportError:
    from pylice import *


def get_license_info(packages=None, output_csv=False):
    """Retrieves license information.

    :param packages: package names
    :type packages: list
    :param output_csv: format output as csv
    :type output_csv: bool
    :return: str
    """
    if packages is not None:
        license_info = [get_license_info_for_distribution(package) for package in packages]
    else:
        license_info = get_license_info_for_working_set()

    license_info.sort(key=lambda x: x[0])

    output = StringIO()
    if output_csv:
        writer = csv.writer(output)
        writer.writerows([info for info in license_info])
    else:
        output.writelines([" ".join(info) + "\n" for info in license_info])

    return output.getvalue()


def main():
    parser = argparse.ArgumentParser("Retrieves license information for installed Python packages.")

    parser.add_argument("--package", dest="packages", action="append",
                        help="Retrieve license for a single Python package")
    parser.add_argument("--output-csv", dest="output_csv", action="store_true",
                        help="Output in CSV format")

    args = parser.parse_args()

    try:
        output = get_license_info(packages=args.packages, output_csv=args.output_csv)
    except Exception as ex:
        sys.stderr.write(str(ex) + "\n")
        sys.exit(1)

    sys.stdout.write(output)
    sys.exit(0)


if __name__ == "__main__":
    main()