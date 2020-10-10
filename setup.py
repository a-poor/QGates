import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qgates",
    version="0.0.1",
    author="Austin Poor",
    author_email="austinpoor@gmail.com",
    description="Helper library for quantum matrix math",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/QGates",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)