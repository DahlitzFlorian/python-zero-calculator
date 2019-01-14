from calculator.helper import stack
from pytest import fail


def test_stack_push():
    """
    Create an empty stack, pushes elements to it and compares the
    expected result with the actual property.
    """
    s = stack.Stack()
    solution = ["Hello", "World", 42]

    s.push("Hello")
    s.push("World")
    s.push(42)

    assert s.stack == solution


def test_stack_pop_non_empty():
    """
    Create an empty stack, pushes elements to it, removes elements and
    compares the expected result with the actual property.
    """
    s = stack.Stack()
    solution = [True, "World", 42]

    s.push(True)
    s.push("World")
    s.push(42)
    s.push(13.0)
    s.pop()

    assert s.stack == solution


def test_stack_pop_empty():
    """
    Try to pop the most recently added element from an empty stack.
    """
    s = stack.Stack()

    try:
        s.pop()
    except IndexError:
        fail("An IndexError was raised, which should never happen.")


def test_stack_peek_non_empty():
    """
    Create an empty stack, pushes elements to it, removes elements and
    takes the most recently added element to compare it to the expected
    result.
    """
    s = stack.Stack()
    solution = 42

    s.push(True)
    s.push("World")
    s.push(42)
    s.push(13.0)
    s.pop()

    assert s.peek() == solution


def test_stack_peek_empty():
    """
    Create an empty stack, tries to take the most recent element and
    compares it to the expected result.
    """
    s = stack.Stack()
    solution = None

    assert s.peek() == solution


def test_stack_is_empty_non_empty():
    """
    Test a given non-empty stack if it's empty.
    """
    s = stack.Stack()
    solution = False

    s.push("Hello World")

    assert s.is_empty() == solution


def test_stack_is_empty_empty():
    """
    Test a given empty stack if it's empty.
    """
    s = stack.Stack()
    solution = True

    assert s.is_empty() == solution


def test_stack_from_list():
    """
    Create a stack from a list and compares it to the expected result.
    """
    elements = [42, "23", False, "Penguin"]
    solution = ["Penguin", False, "23", 42]

    s = stack.Stack().create_from_list(elements)

    assert s.stack == solution


def test_stack_from_empty_list():
    """
    Create a stack from an empty list and compares it to the expected
    result.
    """
    elements = []
    solution = []

    s = stack.Stack().create_from_list(elements)

    assert s.stack == solution
