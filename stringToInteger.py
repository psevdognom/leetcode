#https://leetcode.com/problems/string-to-integer-atoi/
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

class Solution:
    def myAtoi(self, s: str) -> int:
        result = ''
        for symbol in s:
            if symbol.isnumeric() or symbol in ['-', '+']:
                result += str(symbol)
        if result:
            if str(result[0]) == '-':
                result = result[1:]
                result = -1 * int(result)
            elif str(result[0]) == '+':
                result = result[1:]
                result = int(result)
            return int(result)
        else:
            return 0

text = '     -42'
sol = Solution()
print(sol.myAtoi(text)) #42