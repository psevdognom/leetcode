#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return
            for letter in phone[digits[index]]:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
        combinations = []
        backtrack(0, [])
        return combinations