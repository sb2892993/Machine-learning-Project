from setuptools import setup, find_packages
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
        return requirement_file.readlines()  # this returns libraries as a list 
    

setup(
name= project_name,
version=VERSION,
author = AUTHOR,
description=Description,
packages=find_packages(),#["housing"] #inbuilt function,going to return all the folders where we've have
#__init type of folders. any folder which has __init__.py is called module,housing is called package
install_requires=get_requirements_list() # along with packages we require libraries so we're calling that here
)

