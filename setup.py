# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
exec(open('nanocomp/version.py').read())

setup(
    name='NanoComp',
    version=__version__,
    description='Plotting suite for Oxford Nanopore sequencing data and alignments',
    long_description=open(path.join(here, "README.rst")).read(),
    url='https://github.com/wdecoster/NanoComp',
    author='Wouter De Coster',
    author_email='decosterwouter@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='nanopore sequencing plotting quality control',
    packages=find_packages(),
    install_requires=['pandas',
                      'numpy',
                      'nanoplotter>=0.13.5',
                      'nanoget>=0.12.0',
                      'nanomath>=0.12.5'
                      ],
    package_data={'NanoComp': []},
    package_dir={'NanoComp': 'NanoComp'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'NanoComp=nanocomp.NanoComp:main',
        ],
    },
)