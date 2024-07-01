# https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n - 2):
            if 0 not in [x & 1 for x in arr[i:i+3]]:
                return True
        return False
