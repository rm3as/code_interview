class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s: # 文字列を前から順番に見ていく
            
            #左かっこだったらstackに追加
            if c in "({[" :
                stack.append(c)
                
            # 右かっこだったら、
            # 1.stackの一番上の文字が対応する左かっこの場合、stackの一番上の文字を消去
            # 2-1.stackの一番上の文字がそもそもない(stackが空)場合、return False
            # 2-2.stackの一番上の文字が対応しない左かっこの場合、return False
            else:
                if stack==[] or \
                    (c==")" and stack[-1]!="(") or \
                    (c=="}" and stack[-1]!="{") or \
                    (c=="]" and stack[-1]!="["):
                        return False
                
                stack.pop()
                
        return stack==[]
                
            