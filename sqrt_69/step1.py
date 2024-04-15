class Solution:
    def mySqrt(self, x: int) -> int:
        root = 1

        while(1):
            if x == root ** 2:
                return root
            
            elif x < root ** 2:
                return root-1    
            
            root += 1

            
            
            
            
            