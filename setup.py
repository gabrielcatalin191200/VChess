from setuptools import setup, find_packages

setup(
    name='gym_hnef',
    version='0.0.1',
    packages=find_packages(),  # Explicitly specify the packages
    install_requires=['gym']  # And any other dependencies Hnef needs
)
