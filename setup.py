from distutils.core import setup
import os

version = {}

def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)
    return open(path).read()

setup(
    name='audio2numpy',
    version=version['__version__'],
    packages=['audio2numpy'],
    license='MIT',
    author='Jiajun Yang'
    author_email='thejyang@gmail.com'
    long_description=_read('README.md'),
    keywords=['audio, audio reader'],
    url='https://github.com/wiccy46/audio2numpy',

)