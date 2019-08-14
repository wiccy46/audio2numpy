from setuptools import setup
import os
import codecs
from os.path import join

project_root = os.path.dirname(os.path.abspath(__file__))

version = {}
with open(join(project_root, 'audio2numpy/version.py')) as read_file:
    exec(read_file.read(), version)

with open(join(project_root, 'requirements.txt')) as read_file:
    REQUIRED = read_file.read().splitlines()

with open(join(project_root, 'requirements_test.txt')) as read_file:
    REQUIRED_TEST = read_file.read().splitlines()

with codecs.open(join(project_root, 'README.md'), 'r', 'utf-8') as f:
    LONG_DESC = ''.join(f.readlines())

setup(
    name='audio2numpy',
    version=version['__version__'],
    packages=['audio2numpy'],
    license='MIT',
    author='Jiajun Yang',
    author_email='thejyang@gmail.com',
    install_requires=REQUIRED,
    tests_require=REQUIRED_TEST,
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    keywords=['audio, audio reader'],
    url='https://github.com/wiccy46/audio2numpy',
    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)