class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        y=s.split()
        z=len(y)
        m=y[z-1:]
        x=''
        x=x.join(m)
        
        return len(x)