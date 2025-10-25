from setuptools import setup, find_packages



setup(
    name="nrvplinet",
    version="1.0.0",
    url='https://github.com/NRV-framework/pipeline_dev.git',
    author="the NRV framework contributors",
    description='A sample Python project for NRV framework pipeline development',
    packages=find_packages(where="src"),
    package_dir={"": ""
    ""},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)