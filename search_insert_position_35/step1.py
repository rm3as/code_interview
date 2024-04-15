from typing import List
# テストケース
# 0 [4] -> 0

# 3 [-4, -2, 5, 6, 7] -> 2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        target_i = 0
        # 二分探索
        while(1):
            middle_i = len(nums) // 2
                  
            if nums == []:
                return target_i
            elif len(nums) == 1:
                if target > nums[0]:
                    return target_i+1
                else:
                    return target_i
                
            if target == nums[middle_i]:
                target_i += middle_i
                return target_i
            elif target > nums[middle_i]:
                target_i += middle_i
                nums[:middle_i] = []
            else:
                nums[middle_i:] = []
                
                
            
            
            