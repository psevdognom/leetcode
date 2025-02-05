#https://leetcode.com/problems/integer-to-roman/
#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        result = ''
        for value in sorted(roman_numerals.keys(), reverse=True):
            while num >= value:
                result += roman_numerals[value]
                num -= value
        return result

    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        result = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in roman_numerals:
                result += roman_numerals[s[i:i+2]]
                i += 2
            else:
                result += roman_numerals[s[i]]
                i += 1
        return result