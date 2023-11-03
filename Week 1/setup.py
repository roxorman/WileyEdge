from setuptools import setup, find_packages


setup(
    name="firstday",
    version="0.1.0",
    description="this is trailer of how we create and deploy python project",
    author="Marco",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[]
)
