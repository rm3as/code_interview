from typing import List
# "remove the duplicates in-place"と問題文に書いてあるのですが、numsは書き換えなくてよいのでしょうか？
# テストケース
# [2]
# [1,6,8]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]: # 一個前の数と同じ数だった
                
                continue
            i
        return k
        