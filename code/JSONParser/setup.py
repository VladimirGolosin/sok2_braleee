from setuptools import setup, find_packages

setup(
    name="tim3-json-parser",
    version="0.1",
    packages=find_packages(),
    install_requires=['tim3-core>=0.1'],
    entry_points = {'parsiranje':
            ['json_parse=JSONParser.kod.parse:JSONParser']},
    zip_safe=True
)