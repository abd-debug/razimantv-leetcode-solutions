# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        ret, cur = 0, 0
        for i, c in enumerate(s):
            if c == 'b':
                cur += 1
            ret = min(ret, 2 * cur - i - 1)
        return ret + len(s) - cur
