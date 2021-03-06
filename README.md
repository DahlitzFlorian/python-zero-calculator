# Zero Calculator #
[![Build Status](https://travis-ci.org/DahlitzFlorian/python-zero-calculator.svg?branch=master)](https://travis-ci.org/DahlitzFlorian/python-zero-calculator)
![black](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Docker Automated Build](https://img.shields.io/badge/docker%20build-automated-blue.svg)](https://cloud.docker.com/u/floriandahlitz/repository/docker/floriandahlitz/python-zero-calculator)
## Description ##
This package includes a basic zero calculator implemented in Python.
It's using bisectioning to compute the zero in a given interval. It was
developed more for educational purposes than for productive usage.

version 0.3.1

## Features ##
### Available ###
By know you are able to calculate certain things by importing the
package. Examples are provided beneath.

```python3
>>> from calculator.calculator import Calculator
>>> func = "2 ** 3 + 9 / 3"
>>> c = Calculator(func)
>>> c.evaluate()
11
```

```python3
>>> from calculator.calculator import Calculator
>>> func = "x ** 3 + 8 / x"
>>> c = Calculator(func, 2)
>>> c.evaluate()
12
```

### Planned ###
- Zero Calculation using bisectioning

## Using Docker ##
If you want to test the package without messing up your local
dependencies, use docker instead:

```PowerShell
$ git clone <repo_url>
$ cd python-zero-calculator
$ docker image build -t zero-calculator .
$ docker container run -it --rm --name zero zero-calculator
```

And from within the REPL import the package:

```python3
>>> from calculator import calculator
```

## Contribute ##
All contributions are welcomed. Make sure, that your Code is
[PEP8](https://www.python.org/dev/peps/pep-0008/) compliant. While
developing this project [flake8](http://flake8.pycqa.org/en/latest/)
was used as Python linter. Using [Black](https://github.com/ambv/black)
simplifies that.

If you want to report any issues, make use of the [Issue Tracker](https://github.com/DahlitzFlorian/python-zero-calculator/issues) provided by GitHub.
