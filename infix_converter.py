from stack import Stack
class InfixConverter:
    def __init__(self, infix_expression):
        self.stack = Stack()
        self.tokens = infix_expression.split()