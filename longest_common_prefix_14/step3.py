from typing import List
# テストケース
# ["a"]
# ["a", "b"]
# ["", "a"]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # 最も短い文字列の文字数分だけfor文回す
        min_len = min(len(s) for s in strs)
        
        for i in range(min_len):
            # i番目の文字が全ての文字列で一致しなければansを更新せず終了
            if any(strs[0][i] != s[i] for s in strs):
                return ans
            else:
                ans += strs[0][i]
        
        return ans