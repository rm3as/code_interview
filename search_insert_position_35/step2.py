from typing import List
# テストケース
# 0 [4] -> 0
# 3 [-4, -2, 5, 6, 7] -> 2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        target_i = None
        low_i, high_i = 0, len(nums)
        while(1):
            mid_i = (low_i + high_i) // 2
            
            if low_i == high_i:
                target_i = low_i
                return target_i
            
            if target == nums[mid_i]:
                target_i = mid_i
                return target_i
            elif target > nums[mid_i]:
                low_i = mid_i + 1
            elif target < nums[mid_i]:
                high_i = mid_i
    
            