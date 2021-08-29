"""Setup script."""

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    line.strip()
    for line in open(os.path.join(here, "requirements.txt"), "r").readlines()
]

setup(
    name="we-plugins-arango-storage",
    version="20210828",
    description="Workflow Executor arango storage plugin.",
    long_description=
    "Store results from workflow executor to be stored in an arango datbase.",
    classifiers=["Programming Language :: Python"],
    author="Kashif Iftikhar",
    author_email="kashif@compulife.com.pk",
    url="https://github.com/kashifpk/we-plugins-arango-storage",
    keywords="Workflow Executor Arango Storage Plugin",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    # entry_points={'console_scripts': ['we = we.we_cmd:cli']},
)
