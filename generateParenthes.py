#https://leetcode.com/problems/generate-parentheses/description/


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        ans = []
        backtrack('', 0, 0)
        return ans