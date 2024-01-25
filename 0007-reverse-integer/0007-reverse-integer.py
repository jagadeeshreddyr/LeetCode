class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False
        
        if x<0:
            negative =  True
            x = -x 
        res = 0
        while x:
            
            res = res*10 + x%10
            
            x//=10
            
        if res >= 2**31-1 or res<=-2**31:
            return 0
        return -res if negative else res