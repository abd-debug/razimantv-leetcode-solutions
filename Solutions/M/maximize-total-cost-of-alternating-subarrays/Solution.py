# https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n, dp1, dp2 = len(nums), nums[-1], 0
        for i in range(n-2, -1, -1):
            dp1, dp2 = nums[i] + max(dp1, dp2 - nums[i+1]), dp1
        return dp1
