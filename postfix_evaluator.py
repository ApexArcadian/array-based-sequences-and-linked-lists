
from stack import Stack



class PostfixEvaluator:
    def __init__(self, postfix_expression):
        self.stack = Stack()
        self.tokens = postfix_expression.split()

    def is_operator(self, token):
        return token in ['+', '-', '*', '/']
    
    def apply_operator(self, operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError("division by zero")
            return operand1 / operand2
        
    def evaluate(self):
        for token in self.tokens:
            if self.is_operator(token):
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = self.apply_operator(token, operand1, operand2)
                self.stack.push(result)
            else:
                try:
                    number = float(token)
                    self.stack.push(number)
                except ValueError:
                    raise ValueError(f"invalid token: {token}")
                
        if self.stack.size() != 1:
            raise ValueError("invalid postfix expression")
        
        return self.stack.pop()