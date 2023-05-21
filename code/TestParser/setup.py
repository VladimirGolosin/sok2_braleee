from setuptools import setup, find_packages

setup(
    name="tim3-test-parser",
    version="0.1",
    packages=find_packages(),
    install_requires=['tim3-core>=0.1'],
    entry_points = {
        'test.load':
            ['parse-dummy=testParser.kod.parse:ParseDummy'],
    },
    zip_safe=True
)