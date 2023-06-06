from setuptools import setup, find_packages

setup(
    name="tim3-complex-visualizer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'vizualizacija':
            ['complex=ComplexVisualizer.complexvisualizer:ComplexVisualizer'], },
    data_files=[('ComplexVisualizer/templates', ['ComplexVisualizer/templates/visualizer_complex.html'])],
    zip_safe=False
)