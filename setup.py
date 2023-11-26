from setuptools import setup, find_packages

setup(
    name='rlbolt',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here.
        # For example, 'numpy', 'torch', etc.
    ],
    # Additional metadata about your package.
    author="Samyakh Tukra",
    description="A brief description of your library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SamPlvs/rlbolt",
)
