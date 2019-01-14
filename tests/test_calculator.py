from calculator import calculator


def test_calculator_simple_evaluate_without_arg():
    """
    Test the calculator with a very basic function not containing
    functions like sin() or cos(). No parameter is specified for evaluate.
    """
    func = "x * x - 2"
    x = 4
    solution = 14

    c = calculator.Calculator(func, x)

    assert c.evaluate() == solution


def test_calculator_simple_evaluate_with_arg():
    """
    Tests the calculator with a very basic function not containing
    functions like sin() or cos(). A parameter is specified for evaluate.
    """
    func = "x ** x - 8"
    x = 3
    solution = 19

    c = calculator.Calculator(func)

    assert c.evaluate(x) == solution


def test_calculator_complex_evaluate_without_arg():
    """
    Tests the calculator with a more complex function containing
    functions like sin() or cos(). No parameter is specified for evaluate.
    """
    func = "sin(pi) + x * 3"
    x = 8
    solution = 24

    c = calculator.Calculator(func, x)

    assert c.evaluate() == solution


def test_calculator_complex_evaluate_with_arg():
    """
    Tests the calculator with a more complex function containing
    functions like sin() or cos(). A parameter is specified for evaluate.
    """
    func = "sin(pi) + x * 3"
    x = 8
    solution = 24

    c = calculator.Calculator(func)

    assert c.evaluate(x) == solution
