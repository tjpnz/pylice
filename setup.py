from distutils.core import setup

setup(
    name='pylice',
    version='0.1.0',
    packages=['pylice', 'pylice.test'],
    url='https://github.com/tjpnz/pylice',
    license='MIT',
    author='Thomas Prebble',
    author_email='thomas.prebble@gmail.com',
    description='Retrieves license information for installed Python packages.',
    entry_points={
        'console_scripts': ['pylice = pylice.main:main']
    }
)
