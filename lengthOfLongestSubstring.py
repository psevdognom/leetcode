#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_letters_in_substring = {s[0]}
        longest_unique_substring = s[0]
        max_length = 1
        for i in range(1, len(s)-1):
            if s[i] not in unique_letters_in_substring:
                unique_letters_in_substring.add(s[i])
                if len(unique_letters_in_substring)> max_length:
                    longest_unique_substring = f"{longest_unique_substring}{i}"
                    max_length = len(unique_letters_in_substring)
            else:
                if s[i] != s[i-1]:
                    longest_unique_substring = f'{s[i-1]}{s[i]}'
                else:
                    longest_unique_substring = s[i]
                unique_letters_in_substring = {letter for letter in longest_unique_substring.split()}
        return max_length