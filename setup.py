from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pysurfline',
    version="0.0.1",
    description="python client to Surfline API",
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/giocaizzi/pysurfline',
    author='giocaizzi',
    author_email='giocaizzi@gmail.com',
    license="MIT",
    packages=find_packages(include=['pysurfline','pysurfline/*']),
    setup_requires=[],
    tests_require=['pytest',"pytest-cov"],
    install_requires=[
        ],   
    extras_require={
        "docs":[],
        "dev":[],
        },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        'Documentation':'',
        'Bug Reports': 'https://github.com/giocaizzi/pysurfline/issues',
        'Source': 'https://github.com/giocaizzi/pysurfline',
    },
)