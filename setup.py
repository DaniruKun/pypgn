from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pypgn',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.3.0',
    packages=['pypgn'],
    url='https://github.com/DaniruKun/pypgn',
    license='MPL-2.0',
    author='Daniils Petrovs',
    author_email='thedanpetrov@gmail.com',
    keywords=['pgn', 'chess', 'game', 'notation'],
    description='Library for parsing and manipulating PGN format files.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
      ],
)
