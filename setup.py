from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will returns the list of requirements
    '''

requirements=[]
with open('requirements.txt') as file_obj:
    requirements=file_obj.readlines()
    requirements =[req.replace("\n","")for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

setup(
name='ML_Project',
version='0.0.1',
author='Suvarna',
author_email='rakshesuvarna1998@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)