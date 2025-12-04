#https://leetcode.com/problems/longest-common-prefix/description/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ''
        for i in range(len(min(strs, key=len))):
            if len(set([word[i] for word in strs])) == 1:
                prefix += strs[0][i]
            else:
                break
        return prefix

def test_longestCommonPrefix():
    solution = Solution()
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl", 'Test Case 1 Failed'
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == "", 'Test Case 2 Failed'
    assert solution.longestCommonPrefix([""]) == "", 'Test Case 3 Failed'
    assert solution.longestCommonPrefix(["a"]) == "a", 'Test Case 4 Failed'
    assert solution.longestCommonPrefix(["ab", "a"]) == "a", 'Test Case 5 Failed'
    assert solution.longestCommonPrefix(["ab", "a", "abc"]) == "a", 'Test Case 6 Failed'
    assert solution.longestCommonPrefix(["ab", "a", "abc", "ab"]) == "a", 'Test Case 7 Failed'
    assert solution.longestCommonPrefix(["ab", "a", "abc", "ab", "ab"]) == "a", 'Test Case 8 Failed'

    assert solution.longestCommonPrefix(["ab", "a", "abc", "ab", "ab", "ab", "abc"]) == "ab", 'Test Case 10 Failed'
    print('All test cases passed')