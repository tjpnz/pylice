# PyLice

**PyLice** retrieves license information for installed Python packages.

## Installation

### From PyPi

```bash
pip install pylice
```

### From source

```bash
git clone https://github.com/tjpnz/pylice.git
cd pylice
python setup.py sdist
pip install dist/pylice-<version>.tar.gz
```

## Usage

Running ```pylice``` without any arguments lists all packages on the Python path along with the license:

```bash
pylice
Blogofile-0.8b1 MIT
Flask-0.10.1 BSD
FormEncode-1.2.6 PSF
```

It's also possible to retrieve license information for a subset of packages by specifying --package one or more times.

PyLice can also output lists in CSV format:

```bash
pylice --output-csv
Blogofile-0.8b1,MIT
Flask-0.10.1,BSD
FormEncode-1.2.6,PSF
```

## Motivation

Many organisations developing commercial software will have policies regarding which licenses are acceptable when making use of third party tools and libraries. Such policies will often prohibit the use of libraries licensed under the GPL.

Developers will sometimes be asked to produce a list of all third party libraries their code depends on at various stages of the development cycle. I've found this to be time consuming as there didn't appear to be anything out there that would help automate the process. PyLice aims to streamline that process using the license information available from installed package metadata.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

Copyright © 2011–2015 Thomas Prebble. PyLice is free software, and may be redistributed under the terms specified in the [license](LICENSE).