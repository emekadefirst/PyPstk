from setuptools import setup, find_packages


with open("README.md", "r") as f:
    description = f.read()

setup(
    name="PythonPaystack",
    version="1.0.0",
    long_description= description,
    long_description_content_type= "text/markdown",
    author="Victor Chibuogwu Chukwuemeka aka Emekadefirst",
    author_email="emekadefirst@gmail.com",
    url="https://github.com/emekadefirst/Paystack-Python-2-SDK",
    packages=find_packages(),
    install_requires=[
        "requests>=2.26.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
