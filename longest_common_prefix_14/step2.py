from typing import List
# テストケース
# ["a"]
# ["a", "b"]
# ["", "a"]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # strsの中の最小文字数が何文字か調べる
        min_len = min(len(str) for str in strs)
        
        # 最初の文字列strs[0]のj番目の文字が他の文字列のj番目と一致しなければansを更新せずに終了
        for j in range(min_len):
            if any(strs[0][j] != str[j] for str in strs):
                return ans
            else:
                ans += strs[0][j]
        return ans