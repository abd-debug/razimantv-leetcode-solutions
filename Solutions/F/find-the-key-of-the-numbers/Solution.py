# https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        strs = [f'{x:04d}' for x in [num1, num2, num3]]
        return int(''.join(min(s[i] for s in strs) for i in range(4)))
