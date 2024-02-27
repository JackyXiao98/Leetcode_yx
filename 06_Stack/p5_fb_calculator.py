"""

https://leetcode.com/problems/basic-calculator-ii/

227. Basic Calculator II

s = " 31 - 21*3"
stack    num     operator
[]       0       +
[]       31      +
[31]     0       -
[31]     21      -
[31, -21] 0      *
[31, -21] 3      *
[31, -63] 0      #
"""

s = " 31 - 21*3"
s = s + '#'
stack = []
operator = "+"
num  = 0
n = len(s)
i = 0

for c in s:
    if c.isnumeric():
        num = num * 10 + int(c)
        print(c, num)
        continue
    elif c == ' ':
        continue
    elif operator == '+':
        stack.append(num)
    elif operator == '-':
        stack.append(-num)
    elif operator == '*':
        left = stack.pop()
        stack.append(left * num)
    elif operator == '/':
        left = stack.pop()
        stack.append(-(left // num))
    print(c, stack)
    operator = c
    num = 0

res = sum(stack)
print(res)


