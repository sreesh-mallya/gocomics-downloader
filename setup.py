from setuptools import setup, find_packages

setup(
    name='gocomics-downloader',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='',
    author='Sreesh Mallya',
    author_email='sreeshsmallya@gmail.com',
    description='Download comic strips from gocomics.com',
    python_requires='>=3.5',
    install_requires=[
        "beautifulsoup4",
        "click"
    ],
    entry_points={"console_scripts": ['gocomicsd=gocomicsd.gocomicsd:cli']}
)
