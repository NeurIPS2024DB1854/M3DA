import runpy
from pathlib import Path

from setuptools import find_packages, setup


CURRENT_DIR = Path(__file__).parent
NAME = "m3da"

_version_path = CURRENT_DIR / NAME / "__version__.py"
_init = runpy.run_path(_version_path.as_posix())
VERSION = _init["__version__"]


with open("requirements.txt", encoding="utf-8") as file:
    REQUIREMENTS = file.read().splitlines()

with open("README.md", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()

setup(
    name=NAME,
    packages=find_packages(include=(NAME, )),
    include_package_data=True,
    version=VERSION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=REQUIREMENTS,
    python_requires=">=3.10",
)
