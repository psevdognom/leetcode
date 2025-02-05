#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest_palindrome = s[0]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if s[i:j+1] == s[i:j+1][::-1]:
                        if len(s[i:j+1]) > len(longest_palindrome):
                            longest_palindrome = s[i:j+1]
        return longest_palindrome