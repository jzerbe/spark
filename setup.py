from setuptools import find_packages
from setuptools import setup

setup(
    author='Jason Zerbe',
    author_email='jzerbe@vraidsys.com',
    description='spark 1.6.3 paired down to just be an installable python package',
    license='Apache License 2.0',
    name='pyspark',
    packages=find_packages(),
    url='https://github.com/jzerbe/spark',
    version='v1.6.3-pyspark',
    zip_safe=True
)
