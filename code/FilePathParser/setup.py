from setuptools import setup, find_packages

setup(
    name="tim3-filepath-parser",
    version="0.1",
    packages=find_packages(),
    install_requires=['tim3-core>=0.1'],
    entry_points = {'parsiranje':
            ['filepath_parse=FilePathParser.kod.parse:FilePathParser']},
    zip_safe=True
)