from setuptools import find_packages, setup

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fbr_integration/__init__.py
from fbr_integration import __version__ as version

setup(
	name="fbr_integration",
	version=version,
	description="FBR Digital Invoice Integration",
	author="Taimoor",
	author_email="tymuur@outlook.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
