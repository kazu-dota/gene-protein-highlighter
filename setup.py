#!/usr/bin/env python3
"""
Setup script for Gene/Protein Recognition Tool
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gene-protein-highlighter",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered gene/protein name recognition and Excel highlighting tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gene-protein-highlighter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gene-highlighter=gene_highlighter:main",
        ],
    },
    include_package_data=True,
    keywords="bioinformatics, nlp, gene, protein, recognition, excel, highlighting, scispacy",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/gene-protein-highlighter/issues",
        "Source": "https://github.com/yourusername/gene-protein-highlighter",
        "Documentation": "https://github.com/yourusername/gene-protein-highlighter#readme",
    },
)