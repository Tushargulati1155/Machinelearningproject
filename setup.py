from setuptools import setup, find_packages
#from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.4"
AUTHOR="Tushar Gulati"
DESCRIPTION="ML REGRESSION PROJECT"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME= "requirements.txt"

def get_requirements_list():
    """
    This function will return the list of requirements mentioned 
    in requirements.txt file
    """
    
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list())