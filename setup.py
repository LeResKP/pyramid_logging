from setuptools import setup, find_packages
import sys, os

# Hack to prevent TypeError: 'NoneType' object is not callable error
# on exit of python setup.py test
try:
    import multiprocessing
except ImportError:
    pass

version = '0.0'

setup(name='pyramid_logging',
      version=version,
      description="Advanced logger for pyramid",
      long_description=open('README.rst').read(),
      classifiers=[
        'Framework :: Pyramid',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Topic :: System :: Logging",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
      ],
      keywords='',
      author='Aur\xc3\xa9lien Matouillot',
      author_email='a.matouillot@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      test_suite='nose.collector',
      tests_require=[
          'nose',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
