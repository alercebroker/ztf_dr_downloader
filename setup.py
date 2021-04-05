from setuptools import setup

with open("requirements.txt") as f:
    required_packages = f.readlines()

required_packages = [r for r in required_packages if "-e" not in r]

setup(
    name="ztf_dr_downloader",
    version="1.0.0",
    description="",
    author="ALeRCE Team",
    author_email='contact@alerce.online',
    # packages=["src"],
    scripts=["cli/dr"],
    install_requires=required_packages
)
