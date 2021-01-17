import setuptools
import sutil

with open("README.md", "r") as f:
      long_description = f.read()

setuptools.setup(
    name="sutil",
    version=sutil.__version__,
    author="sheng_xc",
    author_email="sheng_xc@126.com",
    description="some python utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shengxc/sutil",
    license='Apache License 2.0',
    packages=setuptools.find_packages(exclude=["test"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
