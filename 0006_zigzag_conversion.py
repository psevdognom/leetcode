#https://leetcode.com/problems/zigzag-conversion/description/
# P0      I6        N12
# A1   L5 S7    I11 G13
# Y2 A4   H8 R10
# P3      I9
# PAYPALISHIRING
# 0 1 2  3 4 5 6  7  8 9 10 11 12 13
# 0 6 12 1 5 7 11 13 2 4 8  10 3 9

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['' for _ in range(numRows)]
        for i in range(len(s)):
            row = i % (2*numRows-2)
            if row >= numRows:
                row = 2*numRows-2 - row
            rows[row] += s[i]
        return ''.join(rows)