# It does not matter what you leave beyond the returned k (hence they are underscores).
# という指示文をstep1では読み落としていたので、step2ではこれを考慮して書いた
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i+1