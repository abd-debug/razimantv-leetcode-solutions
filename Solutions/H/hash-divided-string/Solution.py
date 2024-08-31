# https://leetcode.com/problems/hash-divided-string/

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        return ''.join(
            chr(ord('a') + sum(ord(c) - ord('a') for c in s[i:i+k]) % 26)
            for i in range(0, len(s), k)
        )
