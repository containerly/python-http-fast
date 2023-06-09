from setuptools import setup

setup(
    name="{{ .Name }}",
    version="1.0",
    py_modules=["{{ .Name }}"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        {{ .Name }}=app:main
    """,
)