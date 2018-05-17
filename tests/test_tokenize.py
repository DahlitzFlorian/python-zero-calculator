from calculator.helper import tokenize


def test_tokenize_simple():
    """
    Tokenizes a very simple function and tests if it's done correctly.
    """
    function = "2 * x - 2"
    solution = ["2", "*", "x", "-", "2"]

    assert tokenize.tokenize(function) == solution


def test_tokenize_complex():
    """
    Tokenizes a more complex function with different whitespaces and
    operators. It also includes functions like sin() and con().
    """
    function = "x*x- 3 /sin( x +3* x) + cos(9*x)"
    solution = ["x", "*", "x", "-", "3", "/", "sin", "(", "x", "+", "3",
                "*", "x", ")", "+", "cos", "(", "9", "*", "x", ")"]

    assert tokenize.tokenize(function) == solution


def test_tokenize_exponential_operator():
    """
    Tests if tokenizing a function including the exponetial operator **
    works as expected and that it does not add two times the multiplication
    operator to the final list.
    """
    function = "2 ** 3 * 18"
    solution = ["2", "**", "3", "*", "18"]

    assert tokenize.tokenize(function) == solution
