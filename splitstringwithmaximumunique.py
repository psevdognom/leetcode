from typing import List

class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(s, start, path):
            if start == len(s):
                ans.append(path)
                return
            for i in range(start, len(s)):
                if s[start:i+1] not in path:
                    backtrack(s, i+1, path + [s[start:i+1]])
        ans = []
        backtrack(s, 0, [])
        return len(max(ans, key=len))



