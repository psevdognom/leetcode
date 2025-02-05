from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            if word in s:
                s = s.replace(word, '')
        if not s:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("applepenapple", ["apple", "pen"]))  # True