# Release Cycle

## Process

* Update your build tools
```
pip install -U setuptools twine wheel
```
* Check/adjust version in `pya/versions.py`
* Update the change log in README.md
* Run tox
```
tox
```
* Remove old releases
```
rm dist/*
```
* Build releases
```
python3 setup.py sdist bdist_wheel 
```
* Publish to test.pypi
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
* [Check](https://test.pypi.org/project/audio2numpy/) the test project page 

* Test install uploaded release
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple audio2numpy
```
* Upload the official release
```
twine upload dist/*
```
* [Check](https://pypi.org/project/audio2numpy/) the public project page 

* Test install uploaded release
```
pip install audio2numpy
```
* Draft a release on [Github](https://github.com/wiccy46/audio2numpy/releases)

## Further Readings 

* [using test.PyPI](https://packaging.python.org/guides/using-testpypi/)
* [packaging](https://packaging.python.org/tutorials/packaging-projects/)