import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="interkonnect",
    version="0.0.1",
    author="wolfy",
    author_email="bhawk11@gamil.com",
    description="My RowdyHacks 2020 Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shitwolfymakes/interkonnect",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)