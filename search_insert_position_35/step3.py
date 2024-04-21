from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        low_i = 0
        high_i = len(nums)
        while(low_i!=high_i):
            
            middle_i = (low_i + high_i) // 2
            
            if target == nums[middle_i]:
                index = middle_i
                return index
            elif target < nums[middle_i]:
                high_i = middle_i
            elif target > nums[middle_i]:
                low_i = middle_i + 1
        
        index = low_i
        
        return index     
            