class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        
        
        result = []
        for i in range(left, right+1):

            flag=True
            for j in str(i):
                if j!='0':
                    if i%int(j)!=0:
                        flag=False
                else:
                    flag=False
                    break   
            if flag:
                result.append(i)
                
                
        return result
        