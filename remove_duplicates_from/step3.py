from typing import List
# "remove the duplicates in-place"と問題文に書いてあるのですが、numsは書き換えなくてよいのでしょうか？
# テストケース
# [2]
# [1,6,8]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_index = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[unique_index]: # 新たにuniqueな要素がでてきた
                unique_index += 1
                nums[unique_index] = nums[i]
        return unique_index+1 