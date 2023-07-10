"""

https://leetcode.com/problems/daily-temperatures/description/

739. Daily Temperatures

"""




"""
Input: [73,74,75,71,69,72,76,73]
stack holds (val, index)

[] <---- (73, 0)
[(73, 0)] <---- (74, 1)
[(74, 1)] <---- (75, 2)
[(75, 2)] <---- (71, 3)
[(75, 2), (71, 3)] <---- (69, 4)
[(75, 2), (71, 3), (69, 4)] <---- (72, 5)
[(75, 2), (72, 5)] <---- (76, 6)
[(76, 6)] <---- (73, 7)
"""



class Solution:
    def dailyTemperatures(self, temperatures):
        # put (val, index) into the monotonic stack
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # print("current stack: ", stack)
            if len(stack) == 0:
                stack.append((temp, i))
            else:
                while stack[-1][0] < temp:
                    prev_id = stack[-1][1]
                    # every time a value pop out, update the result
                    res[prev_id] = i - prev_id
                    # pop every value that is smaller than current temp
                    stack.pop()
                    if len(stack) == 0:
                        break
                stack.append((temp, i))
        return res
