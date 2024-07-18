# setup.py
from setuptools import setup, find_packages

setup(
    name="utibat",
    version="0.3.0",
    author="Marin",
    author_email="utikacbeats@gmail.com",
    description="A CLI tool to display battery information",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/marinkres/utibat",  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        "click",
        "psutil",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "utibat=utibat.utibat:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
