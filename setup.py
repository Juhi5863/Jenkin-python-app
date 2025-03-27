from setuptools import setup, find_packages

setup(
    name="my_python_app",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "my_python_app=app:main",
        ],
    },
)
