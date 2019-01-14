from calculator.helper import tokenize


def test_tokenize_simple():
    """
    Tokenize a very simple function and tests if it's done correctly.
    """
    func = "2 * x - 2"
    solution = ["2", "*", "x", "-", "2"]

    assert tokenize.tokenize(func) == solution


def test_tokenize_complex():
    """
    Tokenize a more complex function with different whitespaces and
    operators. It also includes functions like sin() and con().
    """
    func = "x*x- 3 /sin( x +3* x) + cos(9*x)"
    solution = [
        "x",
        "*",
        "x",
        "-",
        "3",
        "/",
        "sin",
        "(",
        "x",
        "+",
        "3",
        "*",
        "x",
        ")",
        "+",
        "cos",
        "(",
        "9",
        "*",
        "x",
        ")",
    ]

    assert tokenize.tokenize(func) == solution


def test_tokenize_exponential_operator():
    """
    Test if tokenizing a function including the exponential operator **
    works as expected and that it does not add two times the multiplication
    operator to the final list.
    """
    func = "2 ** 3 * 18"
    solution = ["2", "**", "3", "*", "18"]

    assert tokenize.tokenize(func) == solution
