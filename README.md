# Input-Mocker

[![Build Status](https://travis-ci.org/ciotto/input-mocker.svg?branch=master)](https://travis-ci.org/ciotto/input-mocker)
[![Codecov](https://codecov.io/gh/ciotto/input-mocker/branch/master/graph/badge.svg)](https://codecov.io/gh/ciotto/input-mocker)
[![Version](https://badge.fury.io/py/input-mocker.svg)](https://badge.fury.io/py/input-mocker)
[![Py Versions](https://img.shields.io/pypi/pyversions/input-mocker.svg)](https://pypi.python.org/pypi/input-mocker/)
[![License](https://img.shields.io/pypi/l/input-mocker.svg)](https://pypi.python.org/pypi/input-mocker/)
[![Status](https://img.shields.io/pypi/status/input-mocker.svg)](https://pypi.python.org/pypi/input-mocker/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

**input-mocker** is *simple* and *easy-to-use* tool for mocking of prompt functions.

You can mock call to a `sys.stdin.readline in order to programmatically send user input.


## Installation

You can install **input-mocker** from *PyPi*:

`pip install input-mocker`

or from GitHub:

`pip install https://github.com/ciotto/input-mocker/archive/master.zip`


## Usage

Using **input-mocker** is easy:

```
>>> from input_mocker import InputMocker
>>> with InputMocker():
...    raw_input()  # Or input() for Python3
...    raw_input()
...    raw_input()
...    raw_input()
... 
'y'
'n'
'y'
'n'
```

By default **input-mocker** send alternated 'y'/'n' response.

If you want to get random response initialize instance with `random=True` paramiter:

```
>>> from input_mocker import InputMocker
>>> with InputMocker():
...    raw_input()
...    raw_input()
...    raw_input()
...    raw_input()
... 
'y'
'y'
'n'
'y'
```

Is also possible to use a customized set of inputs:

```
>>> with InputMocker(inputs=['Foo', '42']):
...    raw_input('A question: ')
...    raw_input('What's the ultimate answer to life, the universe, and everything? ')
... 
Question: 'Foo'
What's the ultimate answer to life, the universe, and everything? '42'
```

Sometimes probably you'll prefer to use the decorator:

```
>>> import input_mocker
>>> @input_mocker.patch(random=True)
... def my_method():
...    print(raw_input('question 1: '))
...    print(raw_input('question 2: '))
...    print(raw_input('question 3: '))
...    print(raw_input('question 4: '))
... 
>>> my_method()
question 1: y
question 1: y
question 1: y
question 1: n
```

**input-mocker** work with `sys.stdin.readline()`, `input()` and `raw_input()`.


## How to contribute

This is not a big library but if you want to contribute is very easy!

 1. clone the repository `git clone https://github.com/ciotto/input-mocker.git`
 1. install all requirements `make init`
 1. do your fixes or add new awesome features (with tests)
 1. run the tests `make test`
 1. commit in new branch and make a pull request


---


## License

Released under [MIT License](https://github.com/ciotto/input-mocker/blob/master/LICENSE.txt).
