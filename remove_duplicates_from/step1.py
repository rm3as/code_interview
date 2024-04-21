from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = nums[0]
        i = 1
        for j in range(1, len(nums)):
            if nums[i] == prev_num:
                nums.pop(i)
                continue
                
            # nums[i] != prev_num:
            prev_num = nums[i]
            i += 1
                
                
        