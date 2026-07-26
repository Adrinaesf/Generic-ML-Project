from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Read the requirements file and return the package names as a list.

    get_requirements: file[str] -> List[str]
                      requirements.txt -> ['pandas', 'numpy', ...]
    """

    requirements = []

    with open(file_path, "r") as file_obj:
        for line in file_obj:
            line = line.strip()

            if line != "":
                requirements.append(line)

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

## pip is going to do the installation
## setup will just give the information of the 
## project to pip, so pip can download it. 

## Why do we need -e . in requirment.txt
## because when we do pip install -r requirements.txt, 
## we don't want to just have the libraries and packages downloaded
## we want the package to be downloaded as well. 
setup(
    name="Generic-ML-Project",
    version="0.0.1",
    author="Adrina",
    author_email="adrinacad.esf@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)