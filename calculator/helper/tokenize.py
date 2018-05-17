import re


def tokenize(function: str) -> list:
    """
    Return a list of tokens of a mathimatical expression.
    """
    pattern = r"(\b\w*[\.]?\w+\b|\*\*|[()+*%\/\-])"

    return re.findall(pattern, function)
