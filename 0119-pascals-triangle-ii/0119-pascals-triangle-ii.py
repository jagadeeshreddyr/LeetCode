class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        

        dp = [[1]*x for x in range(1,rowIndex+2)]
        
        
        
        
        for i in range(2,rowIndex+1):
            
            for j in range(i):
                
                if (j==0) or (j==i):
                    dp[i][j] = 1
                        
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    
    
                    
                    
        return dp[rowIndex]
        
        