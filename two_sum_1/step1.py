from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = [None]*2
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    output = [i, j]
                    return output
                    