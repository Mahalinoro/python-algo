# Given an array of integers, determine whether there are two distinct indices i and j in the array such that:
# The absolute difference between i and j is at most k
# The absolute difference between nums[i] and nums[j] is at most t

# Example:
# For nums = [1, 3, 1], k = 2, and t = 1, the output should be
# containsNearbyAlmostDuplicate(nums, k, t) = true.

def absoluteDiff(nums, k, t):
    length = len(nums)    

    if nums[0] < 0 and nums[-1] > 0:
        if nums[-1] - nums[0] <= t:
            return True
        return False
    else:
        for i in range(length):
            num = nums[i]
            for j in range(k):
                if abs(nums[i+j]-num) <= t:
                    return True
                return False