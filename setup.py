from setuptools import setup

setup(
    name="{{ .Repository.Name }}",
    version="1.0",
    py_modules=["{{ .Repository.Name }}"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        {{ .Repository.Name }}=app:main
    """,
)