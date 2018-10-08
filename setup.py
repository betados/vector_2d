# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='vector_2d',
    version='1.0.0',
    description='A module witch implements a two-dimensional vector, both in cartesian and polar coordinates.',
    long_description=open('README.MD').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['vector_2D'],
    author='Álvaro Torres Ochaita',
    author_email='torrestal@gmail.com',
    keywords=['vector', '2d', 'physics', 'games', 'pygame'],
    url='https://github.com/betados/vector_2D',
)
# python setup.py sdist bdist_wheel
# twine upload dist/*
