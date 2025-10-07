from setuptools import setup
from typing import List

#declaring variables for setup fn
project_name="housing-predictor"
VERSION= "0.0.1"
AUTHOR="Surendra"
Description="this is the ML PROJECT"
packages=["housing"]
requirement_file_name="requirements.txt"


#we can ignore list[str], this returns the string value ,but best practise to insert
def get_requirements_list()   ->List[str]:

    """"
    Description: this fn is going to return list of requirement 
    mention in requirements.txt file

    return: this function is going to return a list which contain name of libraries 
    mentioned in requirements.txt file
    """

    with open(requirement_file_name) as requirement_file:
        return requirement_file.readlines()
    

setup(
name= project_name,
version=VERSION,
author = AUTHOR,
description=Description,
packages=packages,
install_requires=get_requirements_list()
)

