class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return f"{self.__class__.__name__}({self.stack})"

    def __str__(self):
        return f"{self.stack}"

    def push(self, element):
        """
        Add an element on the top of the stack.
        """
        self.stack.append(element)

    def pop(self):
        """
        Remove the most recently added element of the stack.
        """
        if not self.is_empty():
            self.stack.pop()

    def peek(self):
        """
        Return the most recently added element of the stack.
        If the stack is empty, it returns None.
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        """
        Return a boolean representing the current status of the stack,
        whether it's empty or not.
        """
        return not len(self.stack)

    @staticmethod
    def create_from_list(elements: list) -> "Stack":
        """
        Get a list of elements and creates a stack out of it.
        """
        s = Stack()

        for element in reversed(elements):
            s.push(element)

        return s
