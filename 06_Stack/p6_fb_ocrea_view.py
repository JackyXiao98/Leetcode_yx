"""

https://leetcode.com/problems/buildings-with-an-ocean-view/

1762. Buildings With an Ocean View

heights = [4, 2, 3, 1]

stack = [(4, 0), (3, 2), (1, 3)]
res = [0, 2, 3]

"""

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, h in enumerate(heights):
            while len(stack) > 0 and stack[-1][0] <= h:
                stack.pop()
            stack.append((h, i))
        res = []
        for h, i in stack:
            res.append(i)
        return res
