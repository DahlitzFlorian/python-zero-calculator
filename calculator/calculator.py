import math
import sys

from typing import Union

from calculator.helper import tokenize
from calculator.helper import stack


class Calculator:
    CONSTANTS = {"e", "pi"}
    FUNCTIONS = {"sqrt", "log", "exp", "sin", "cos", "tan"}
    OPERATIONS = {"+", "-", "*", "/", "**"}

    def __init__(self, func: str, x=None):
        self._func = func
        self._tokens = stack.Stack().create_from_list(tokenize.tokenize(func))
        self._operators = stack.Stack()
        self._arguments = stack.Stack()
        self._x = convert_to_number(x) if isinstance(x, str) else x

    def evaluate(self, x=None):
        if self._tokens.is_empty():
            self._tokens = stack.Stack().create_from_list(tokenize.tokenize(self._func))
            self._operators = stack.Stack()
            self._arguments = stack.Stack()

        while not self._tokens.is_empty():
            next_operator = self._tokens.peek()
            self._tokens.pop()

            if next_operator in self.CONSTANTS:
                self._arguments.push(self._get_constant(next_operator))
                continue

            if is_number(next_operator):
                number = convert_to_number(next_operator)
                self._arguments.push(number)
                continue

            if next_operator == "x":
                if x is not None:
                    self._arguments.push(x)
                else:
                    self._arguments.push(self._x)
                continue

            if self._operators.is_empty() or next_operator == "(":
                self._operators.push(next_operator)
                continue

            top_operator = self._operators.peek()

            if top_operator == "(" and next_operator == ")":
                self._operators.pop()
            elif next_operator == ")" or self._eval_before(top_operator, next_operator):
                self._pop_and_evaluate()
                self._tokens.push(next_operator)
            else:
                self._operators.push(next_operator)

        while not self._operators.is_empty():
            self._pop_and_evaluate()

        return self._arguments.peek()

    def _eval_before(self, stack_op: str, next_op: str) -> bool:
        if stack_op == "(":
            return False

        stack_prec = self._get_precedence(stack_op)
        next_prec = self._get_precedence(next_op)

        if stack_prec > next_prec:
            return True
        elif stack_prec == next_prec:
            if stack_op == next_op:
                return stack_op in {"+", "-", "*", "/", "%"}
            return True
        return False

    def _get_precedence(self, operator: str) -> int:
        """
        Gets an operator and returns the respective precedence.
        """
        precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "%": 2,
            "**": 3,
            "exp": 4,
            "log": 4,
            "sqrt": 4,
            "sin": 4,
            "cos": 4,
            "tan": 4,
        }
        assert operator in precedence, f"Invalid operator {operator}."
        return precedence[operator]

    def _pop_and_evaluate(self):
        rhs = int(self._arguments.peek())
        self._arguments.pop()

        op = self._operators.peek()
        self._operators.pop()

        if op in self.FUNCTIONS:
            if op == "sqrt":
                result = math.sqrt(rhs)
            elif op == "log":
                result = math.log(rhs)
            elif op == "exp":
                result = math.exp(rhs)
            elif op == "sin":
                result = math.sin(rhs)
            elif op == "cos":
                result = math.cos(rhs)
            elif op == "tan":
                result = math.tan(rhs)
            self._arguments.push(result)
            return

        lhs = int(self._arguments.peek())
        self._arguments.pop()

        result = 0
        if op == "+":
            result = lhs + rhs
        elif op == "-":
            result = lhs - rhs
        elif op == "*":
            result = lhs * rhs
        elif op == "/":
            result = lhs / rhs
        elif op == "%":
            result = lhs % rhs
        elif op == "**":
            result = lhs ** rhs
        else:
            sys.exit(f"Invalid operator {op}")

        self._arguments.push(result)

    def _get_constant(self, const: str) -> float:
        """
        Gets a string and returns the respective mathematical constant as
        float.
        """
        const = const.lower()
        assert const in self.CONSTANTS, f"Invalid constant {const}."
        if const == "e":
            return math.e
        elif const == "pi":
            return math.pi


def is_number(number: str) -> bool:
    """
    Checks, whether a given string is an int, a float or none of them.
    """
    try:
        float(number)
        return True
    except ValueError:
        try:
            int(number)
            return True
        except ValueError:
            return False


def convert_to_number(number: Union[str, None]) -> Union[int, float]:
    """
    Converts a given string to and int or float respectively.
    """
    if number is None:
        return None

    try:
        number = int(number)
        return number
    except ValueError:
        return float(number)
