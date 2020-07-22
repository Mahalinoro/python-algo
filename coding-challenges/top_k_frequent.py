# Given a non-empty array of integers, return the k most frequent elements

# Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        
        for i in range(len(nums)):
            if nums[i] not in frequency.keys():
                frequency[nums[i]] = 1
            else:
                frequency[nums[i]] += 1
        
        return [h[0] for h in heapq.nlargest(k, frequency.items(), itemgetter(1,0))] 
                