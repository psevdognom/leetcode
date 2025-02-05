class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def convert(s):
            return ''.join(str(ord(ch) - ord('a') + 1) for ch in s)
        s = convert(s)
        for _ in range(k):
            s = str(sum(int(ch) for ch in s))
        return int(s)