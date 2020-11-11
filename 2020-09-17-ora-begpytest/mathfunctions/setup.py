from setuptools import setup, find_packages

setup(
    name='mathfunctions',
    extras_require=dict(test['pytest']),
    packages=find_packages(where='proj'),
    package_dir={"":"proj"}
)