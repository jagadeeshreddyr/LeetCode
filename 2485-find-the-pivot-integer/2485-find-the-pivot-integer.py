class Solution:
    def pivotInteger(self, n: int) -> int:
        
        
        totalsum = n * (n+1) //2 
        
        for i in range(1, n+1):
            
            leftsum = i * (i+1) //2
            
            rightsum = totalsum - ((i-1) * i//2)
            
            
            if leftsum == rightsum:
                return i
            
        return -1