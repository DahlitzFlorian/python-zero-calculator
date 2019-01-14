# Zero Calculator #
[![Build Status](https://travis-ci.org/DahlitzFlorian/python-zero-calculator.svg?branch=master)](https://travis-ci.org/DahlitzFlorian/python-zero-calculator)
![black](https://img.shields.io/badge/code%20style-black-000000.svg)
## Description ##
This package includes a basic zero calculator implemented in Python.<br>
It's using bisectioning to compute the zero in a given interval. It was developed<br>
more for educational purposes than for productive usage.

version 0.2dev

## Features ##
### Available ###
By know you are able to calculate certain things by importing the package. Examples are<br>
provided beneath.

```python3
>>> from calculator.calculator import Calculator
>>> calculation = "2 ** 3 + 9 / 3"
>>> c = Calculator(function)
>>> c.evaluate()
11
```

```python3
>>> from calculator.calculator import Calculator
>>> calculation = "x ** 3 + 8 / x"
>>> c = Calculator(function, 2)
>>> c.evaluate()
12
```

### Planned ###
- Zero Calculation using bisectioning

## Contribute ##
All contributions are welcomed. Make sure, that your Code is [PEP8](https://www.python.org/dev/peps/pep-0008/) compliant.<br>
While developing this project [flake8](http://flake8.pycqa.org/en/latest/) was used as Python linter.

If you want to report any issues, make use of the [Issue Tracker](https://github.com/DahlitzFlorian/python-zero-calculator/issues) provided by GitHub.
