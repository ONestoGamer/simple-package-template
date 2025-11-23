from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_package",
    version="0.0.1",
    author="Ernesto Silva",
    author_email="ernestoo.es@gmail.com",
    description="A package for basic image processing tasks",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ONestoGamer/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
