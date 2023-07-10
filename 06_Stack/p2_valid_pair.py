"""

https://leetcode.com/problems/valid-parentheses/description/

20. Valid Parentheses

Two things to check
1. When adding ')', if the stack is empty, then it's invalid
2. When finished, if the stack is non-empty, then it's invalid
"""



class Solution:
    def isValid(self, s: str) -> bool:
        def is_pair(left, right):
            if left == '(' and right == ')':
                return True
            if left == '[' and right == ']':
                return True
            if left == '{' and right == '}':
                return True
            return False
        
        stack = []
        left_pair = ['(', '[', '{']
        right_pair = [')', ']', '}']

        for c in s:
            if c in left_pair:
                stack.append(c)
            elif len(stack) == 0:
                # c is in right_pair but the stack is empty
                return False
            else:
                left = stack[-1]
                right = c
                if is_pair(left, right):
                    stack.pop()
                else:
                    return False
        
        if len(stack) > 0:
            # there are remaining '(' in the stack
            return False
        else:
            return True
        

