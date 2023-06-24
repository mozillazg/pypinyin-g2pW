# coding: utf-8
from codecs import open
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pypinyin-g2pw",
    version="0.4.0",
    author="mozillazg",
    author_email="mozillazg101@gmail.com",
    description="基于 g2pW 提升 pypinyin 的准确性。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mozillazg/pypinyin-g2pW",
    project_urls={
        "Bug Tracker": "https://github.com/mozillazg/pypinyin-g2pW/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=['g2pw>=0.1.1', 'pypinyin>=0.47.1'],
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.6, <4',
)
