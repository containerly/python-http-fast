from setuptools import setup

setup(
    name="cookiecutter_python_http_fast",
    version="1.0",
    py_modules=["cookiecutter_python_http_fast"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        cookiecutter_python_http_fast=app:main
    """,
)