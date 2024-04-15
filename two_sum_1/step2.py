# テストケース
# {([)}]　false
# {[]}([]) true
    
# 右かっこが先に来たらダメ<＝>a, b, cが負になったらfalse
# 右かっこの数と左かっこの数が違ったらダメ＜＝＞a,b,c!=0ならfalse
# PDA的なイメージ？

class Solution:
    def isValid(self, s: str) -> bool:
        a, b, c = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                a += 1
            elif s[i] == ")":
                a -= 1
                
                    
            elif s[i] == "{":
                b += 1
            elif s[i] == "}":
                b -= 1
            elif s[i] == "[":
                c += 1
            elif s[i] == "]":
                c -= 1

            if a<0 or b<0 or c<0:
                return False
        
        if a==0 and b==0 and c==0:
            return True
        