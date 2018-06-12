from setuptools import setup

setup(name='pyspark',
      version='v1.6.3-pyspark',
      description='spark 1.6.3 paired down to just be an installable python package',
      url='https://github.com/jzerbe/spark',
      author='Jason Zerbe',
      author_email='jzerbe@vraidsys.com',
      license='MIT',
      packages=['pyspark'],
      zip_safe=True)
