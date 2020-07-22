# Given a list of integers nums and an integer k, return the maximum possible i where nums[0] + nums[1] + ...  + nums[i] ≤ k. 
# Return -1 if no valid i exists.

# Example:
# Input: nums = [3, -5, 4, 1, 6], k = 4
# Output: 3

class Solution:
    def solve(self, nums, k):
        sums = {}
        s = 0
        
        for i in range(len(nums)):
            s += nums[i]
            if s <= k:
                sums[i] = s
        
        if sums == {}:
            return -1
        else:
            return list(sums.keys())[-1]