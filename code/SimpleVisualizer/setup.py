from setuptools import setup, find_packages

setup(
    name="tim3-simple-visualizer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'vizualizacija':
            ['simple=SimpleVisualizer.simplevisualizer:SimpleVisualizer'], },
    data_files=[('SimpleVisualizer/templates', ['SimpleVisualizer/templates/visualizer.html'])],
    zip_safe=False
)