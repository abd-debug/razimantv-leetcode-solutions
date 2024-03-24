# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ret, n = 2, len(s)
        for i in range(n):
            for j in range(i + ret - 1, n):
                if max(Counter(s[i:j+1]).values()) < 3:
                    ret = j - i + 1
                else:
                    break
        return ret
