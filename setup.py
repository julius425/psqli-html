import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="psqli-html",
    version="0.0.1",
    author="Julius Kosytskyi",
    author_email="juliusk425@gmail.com",
    description=
    """
    PandasSQLInterface-to-html module.
    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/julius425/psqli-html.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)