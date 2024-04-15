class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s: # 文字列を前から順番に見ていく
            
            #左かっこだったらstackに追加
            if c in "({[" :
                stack.append(c)
                
            
            else:
                pair = {
                    ")": "(",
                    "]": "[",
                    "}": "{"
                }
                if not stack or \
                    (stack[-1] != pair[c]):
                        return False
                
                stack.pop()
                
        return not stack