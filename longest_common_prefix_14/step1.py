from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        temp_ans = ""
        
        # 最初のwordの頭i文字が、他のj番目のwordと共通か確認
        for i in range(len(strs[0])+1):
            temp_ans = strs[0][:i]
            flag = True
            for j in range(1,len(strs)):             
                if len(strs[j]) >= i: # strsのj番目のwordがi文字以上であることを確認
                    # 最初からi番目までが共通か確認
                    if not strs[0][0:i] == strs[j][0:i]:
                        flag = False
                        break
                    elif j == len(strs)-1:
                        flag = True
                else:
                    flag = False
                    break
            if flag:
                ans = temp_ans
        
        return ans    
    

                    
                        
