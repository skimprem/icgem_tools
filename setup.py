from setuptools import setup, find_packages

setup(
    name="icgem-tools",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)