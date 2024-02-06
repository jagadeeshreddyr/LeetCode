class Solution:
    def maximum69Number (self, num: int) -> int:

        y=str(num)
        x=len(y)
        ind=0
        for i in range(x):
            if y[i]=='6':
                ind=i
                
                break 
        return int(y[:ind]+'9'+y[ind+1:])
        