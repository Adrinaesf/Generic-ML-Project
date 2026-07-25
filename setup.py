from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Read the requirements file and return the package names as a list.
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


setup(
    name="Generic-ML-Project",
    version="0.0.1",
    author="Adrina",
    author_email="adrinacad.esf@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)