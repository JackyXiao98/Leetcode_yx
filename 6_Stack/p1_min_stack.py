"""
https://leetcode.com/problems/min-stack/description/

155. Min Stack
"""

class MinStack:

    def __init__(self):
        # each element in the stack is (num, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            # empty stack
            self.stack.append((val, val))
        else:
            previous_min = self.stack[-1][1]
            self.stack.append((val, min(val, previous_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
