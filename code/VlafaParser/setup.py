from setuptools import setup, find_packages

setup(
    name="tim3-vlafa-parser",
    version="0.1",
    packages=find_packages(),
    install_requires=['tim3-core>=0.1'],
    entry_points = {'parsiranje':
            ['dummy_parse_vlafa=vlafaParser.kodd.parse:VlafaParser']},
    zip_safe=True
)