class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}




        count=d[s[-1]]

        prev = d[s[-1]]

        for i in range(len(s)-2, -1,-1):

            if d[s[i]] >= prev:
                count+=d[s[i]]
                prev = d[s[i]]
            else:

                count -= d[s[i]]


        return count