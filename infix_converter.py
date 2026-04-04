from stack import Stack

class InfixConverter:
    def __init__(self, infix_expression):
        self.stack = Stack()
        self.tokens = infix_expression.split()
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        self.right_associative = set()  # All operators are left-associative
    
    def is_operator(self, token):
        """Check if token is an operator"""
        return token in self.precedence
    
    def is_operand(self, token):
        """Check if token is an operand (number or variable)"""
        # If it's an operator or parenthesis, it's not an operand
        if token in self.precedence or token in ['(', ')']:
            return False
        # Otherwise, it's an operand (number or variable name)
        return True
    
    def convert(self):
        """Convert infix expression to postfix using Shunting Yard algorithm"""
        for token in self.tokens:
            if self.is_operand(token):
                # If operand, add to output
                self.output.append(token)
            elif token == '(':
                # If left parenthesis, push to stack
                self.stack.push(token)
            elif token == ')':
                # If right parenthesis, pop operators until matching '('
                while not self.stack.is_empty() and self.stack.peek() != '(':
                    self.output.append(self.stack.pop())
                if self.stack.is_empty():
                    raise ValueError("Mismatched parentheses: missing opening '('")
                self.stack.pop()  # Remove the matching '('
            elif self.is_operator(token):
                # If operator, pop operators with higher or equal precedence (for left-associative)
                while (not self.stack.is_empty() and 
                       self.stack.peek() != '(' and 
                       self.is_operator(self.stack.peek()) and
                       self.precedence[self.stack.peek()] >= self.precedence[token]):
                    self.output.append(self.stack.pop())
                self.stack.push(token)
            else:
                raise ValueError(f"Invalid token: {token}")
        
        # Pop remaining operators from stack
        while not self.stack.is_empty():
            token = self.stack.pop()
            if token == '(' or token == ')':
                raise ValueError("Mismatched parentheses")
            self.output.append(token)
        
        return ' '.join(self.output)