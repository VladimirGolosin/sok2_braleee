from setuptools import setup, find_packages

setup(
    name="tim3-test-parser",
    version="0.1",
    packages=find_packages(),
    install_requires=['tim3-core>=0.1'],
    entry_points = {'parsiranje':
            ['dummy_parse=testParser.kod.parse:DummyParser']},
    zip_safe=True
)