class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        
        for x in range(len(image)):
            ans.append(image[x][::-1])
        
        
        
        for i in range(len(image)):
            for j in range(len(image)):
                if ans[i][j]==1:
                    ans[i][j]=0
                else:
                    ans[i][j]=1
            
        return(ans)
        