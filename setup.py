from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    '''
    The function returns list of requirements
    '''
    EDITABLE = '-e .'
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if EDITABLE in requirements:
            requirements.remove(EDITABLE)
    return requirements

print(get_requirements('requirements.txt'))

setup(
    name='firstproject',
    version = '0.0.1',
    author= 'james',
    author_email = 'rodriguesjames123@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)