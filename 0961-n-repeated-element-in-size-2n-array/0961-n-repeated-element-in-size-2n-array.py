class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        res=0
        
        N=[]
        l=len(A)
        x=0
        
        for i in range(0,l):
            if A[i] not in N:
                N.append(A[i])
            else:
                return(A[i])
        
        
        