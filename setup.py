from setuptools import setup
from reclip import __version__

setup(
    name="reclip",
    version=__version__,
    packages=['reclip'],
    entry_points={
        "console_scripts": [
            "reclip = reclip.__main__:main",
        ],
    }
)
