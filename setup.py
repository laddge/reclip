from setuptools import setup
from reclip import __version__

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name='reclip',
    version=__version__,
    description='a clipboard server',
    long_description=readme,
    url='https://github.com/laddge/reclip',
    author='Laddge',
    author_email='dev.laddge@gmail.com',
    licence='MIT',
    packages=['reclip'],
    entry_points={
        'console_scripts': [
            'reclip = reclip.__main__:main',
        ],
    }
)
