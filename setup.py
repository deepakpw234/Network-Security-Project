from setuptools import setup,find_packages



HYPON_DOT_E = "-e ."
def get_required_details(file_name):
    # Reading from the requirements file

    with open(file_name,"r") as file:
        requirements = file.read().splitlines()

    if HYPON_DOT_E in requirements:

        requirements.remove(HYPON_DOT_E)

    return requirements


setup(
    name="Network Security APP",
    version="0.0.1",
    description="This is a network security app",
    long_description="This is a network security app whose aim is to solve the network security issues in the real time.This app uses ETL pipeline for real time data and mlflow for experiments tracking",
    author="Deepak Pawar",
    author_email="deepakpw234@gmail.com",
    packages=find_packages(),
    install_requirements = get_required_details('requirements.txt'),
    
)
