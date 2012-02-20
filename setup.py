#!/usr/bin/env python
from distutils.core import setup, Extension
try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

import deap

deap_ctools = Extension('deap.cTools', ['deap/cTools.cpp'])

setup(name='deap',
      version=deap.__revision__,
      description='Distributed Evolutionary Algorithms in Python',
      long_description=open('README.txt').read(),
      author='deap Development Team',
      author_email='deap-users@googlegroups.com',
      url='http://deap.googlecode.com',
      download_url='http://code.google.com/p/deap/downloads/list',
      packages=['deap', 'deap.benchmarks', 'deap.dtm', 'deap.tests'],
      platforms=['any'],
      keywords=['evolutionary algorithms','genetic algorithms','genetic programming','cma-es','ga','gp','es','pso'],
      license='LGPL',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        ],
     ext_modules = [deap_ctools],
     cmdclass = {'build_py': build_py}
)
