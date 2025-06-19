'''
this setup.py file is an essential part of packaing and distributing python projexts
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return list of string that contains all the required packages
    '''
    requirement_list:List[str]=[]
    try:
        with open("requirements.txt", "r") as f:
            lines=f.readlines()
            ## process
            for line in lines:
                requirement = line.strip()
                ## ignore empty line and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list





setup(
    name='Network security',
    version='0.0.1',
    author="abhiram",
    author_email="abhiramgajula9@gmial.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
