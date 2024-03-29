from setuptools import setup, find_packages

setup(
    name="tim3-csv-parser",
    version="0.1",
    packages=find_packages(),
    install_requires=['tim3-core>=0.1'],
    entry_points = {'parsiranje':
            ['csv_parse=CSVParser.kod.parse:CSVParser']},
    zip_safe=True
)