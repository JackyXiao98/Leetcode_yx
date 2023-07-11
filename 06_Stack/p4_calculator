"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

150. Evaluate Reverse Polish Notation
"""


def evalRPN(self, tokens) -> int:
        
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }
    
    stack = []
    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1, number_2))
        else:
            stack.append(int(token))
    return stack.pop()
