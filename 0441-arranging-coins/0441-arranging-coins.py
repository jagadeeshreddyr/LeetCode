class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        
        k = 1
        while n>=k:
    
            n = n-k
            k+=1
            
        
        return k-1