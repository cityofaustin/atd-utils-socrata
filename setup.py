import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="socratautil",
    version="0.0.1",
    author="City of Austin",
    author_email="transportation.data@austintexas.gov",
    description="Utilities interacting with the Socrata Open Data API.",
    install_requires=[
        "requests",
        "git+https://github.com/cityofaustin/atd-utils-data.git@master@egg=datautil-0"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cityofaustin/atd-utils-socrata",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", 
    ),
)

