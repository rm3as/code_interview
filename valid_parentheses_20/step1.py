# テストケース
# {([)}]　false
# {[]}([]) true
    
# PDA的なイメージ？

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
       
        for i in range(len(s)):
            if s[i]== "(" or s[i]== "{" or s[i]== "[": # 左かっこが出てきた
                stack.append(s[i])
            else: # 右かっこが出てきた
                if stack==[] or \
                    (s[i]==")" and stack[-1]!="(") or \
                    (s[i]=="}" and stack[-1]!="{") or \
                    (s[i]=="]" and stack[-1]!="["):
                        return False
                
                stack.pop()
        
        if stack == []:
            return True
        else:
            return False
