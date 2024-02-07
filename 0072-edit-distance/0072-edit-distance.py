class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        
        m = len(word1)
        n = len(word2)
        
        if m == 0:
            return n
        
        array= [[0] * (n + 1) for _ in range(m + 1)]
        
        
        for i in range(m+1):
            array[i][0] = i
            
        for j in range(n+1):
            array[0][j] = j
            
        
        for i in range(1, m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    array[i][j] = array[i-1][j-1]
                else:
                    array[i][j] = min(array[i-1][j], array[i-1][j-1], array[i][j-1])+1
                
        return array[m][n]
                     
                     
                      