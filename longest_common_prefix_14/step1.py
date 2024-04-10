from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        
        # 最初のwordの頭i文字が、他のj番目のwordと共通か確認
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):             
                if len(strs[j]) >= i: # strsのj番目のwordがi文字以上であることを確認
                    # 最初からi番目までが共通か確認
                    if not strs[0][0:i] == strs[j][0:i]:
                        break
                    if j == len(strs)-1:
                        ans = strs[0][0:i]
        
        return ans    

    

                    
                        
