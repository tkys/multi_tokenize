from setuptools import setup, find_packages
import subprocess

INSTALL_REQUIRES = [
    "wheel",
    "icu-tokenizer>=0.0.1",
    "PyICU>=2.9",
    "regex>=2022.9.13",
    "SudachiDict-core>=20220729",
    "SudachiPy>=0.6.6",
    "tqdm"
]

setup(
    name='multi_tokenize',
    version='0.1',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES
    
)
