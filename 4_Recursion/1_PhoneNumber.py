# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:56:21 2020.

@author: 10259

Facebook Recursion 1
"""

num_to_char = {}
num_to_char['2'] = ['a', 'b', 'c']
num_to_char['3'] = ['d', 'e', 'f']
num_to_char['4'] = ['g', 'h', 'i']
num_to_char['5'] = ['j', 'k', 'l']
num_to_char['6'] = ['m', 'n', 'o']
num_to_char['7'] = ['p', 'q', 'r', 's']
num_to_char['8'] = ['t', 'u', 'v']
num_to_char['9'] = ['w', 'x', 'y', 'z']

input_num = '237'
list_char = []
word = ''

size_num = len(input_num)
index_num = 0


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map
            # the next available digit
            for letter in phone[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output
