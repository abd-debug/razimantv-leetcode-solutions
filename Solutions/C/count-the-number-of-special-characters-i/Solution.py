# https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ret = 0
        for i in range(26):
            a, A = chr(ord('a') + i), chr(ord('A') + i)
            if a in word and A in word:
                ret += 1
        return ret
