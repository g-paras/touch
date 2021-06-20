from sys import version
from setuptools import setup

setup(
    name="touch",
    version="0.0.1",
    packages=["touch"],
    url="",
    license="",
    author="Paras Gupta",
    author_email="guptaparas039@gmail.com",
    description="touch command for Windows",
    entry_points={
        'console_scripts': ['touch=touch.cli:create_file'],
    }
)
