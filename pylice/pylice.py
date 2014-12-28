import pkg_resources


def __extract_license(dist):
    """Extracts license information from PKG-INFO metadata. Returns "UNKNOWN" if no license can be found.

    :param dist: the distribution
    :type dist: pkg_resources.Distribution
    :return: license (str) or None
    """
    if not dist.has_metadata("PKG-INFO"):
        return "UNKNOWN"

    for line in dist.get_metadata_lines("PKG-INFO"):
        try:
            (meta_key, meta_value) = line.split(": ", 1)
        except ValueError:
            # Malformed metadata line
            continue
        if meta_key == "License":
            return meta_value


def get_license_info_for_working_set():
    """Gets license info for all packages on Python path.

    :return: list of tuple (name-version, license)
    """
    license_info = []
    for working_set in pkg_resources.working_set:
        try:
            dist = pkg_resources.require(working_set.key)[0]
        except pkg_resources.DistributionNotFound:
            # Most likely a consistency issue within site packages.
            continue

        _license = __extract_license(dist)

        license_info.append(("%s-%s" % (dist.project_name, dist.version), _license))

    return license_info


def get_license_info_for_distribution(dist_spec):
    """Gets license info for a specific distribution.

    :param dist_spec: distribution spec
    :type dist_spec: str
    :return: tuple (name-version, license) or None if distribution not found
    """
    try:
        dist = pkg_resources.require(dist_spec)[0]
    except pkg_resources.DistributionNotFound:
        raise Exception("No distribution could be found for %s" % dist_spec)

    _license = __extract_license(dist)

    return "%s-%s" % (dist.project_name, dist.version), _license,