
from setuptools import setup, find_packages

setup(
    name="nutribr",
    version="0.1.0",
    description="Biblioteca nutricional baseada na TACO/IBGE com VDR, filtros e CLI.",
    author="Pedro Richil",
    author_email="pedro@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "nutribr=nutribr.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
