from distutils.core import setup
from setuptools import find_packages

setup(
    name='pylice',
    version='0.1.0',
    packages=find_packages(exclude=['pylice.test']),
    url='https://github.com/tjpnz/pylice',
    license='MIT',
    author='Thomas Prebble',
    author_email='thomas.prebble@gmail.com',
    description='Retrieves license information for installed Python packages.',
    long_description='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='versioning',
    install_requires=[],
    entry_points={
        'console_scripts': ['pylice = pylice.main:main']
    }
)
