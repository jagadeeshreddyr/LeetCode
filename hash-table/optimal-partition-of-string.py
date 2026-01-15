class Solution:
    def partitionString(self, s: str) -> int:

        d = {}
        count = 1

        for j in s:
            # print(type(i))

            if j not in d:

                d[j] = 1 
                
            else:
                count+=1
                d = {j:1}

        #         t = i
        #         d+=1
        # rep +=rep+t

        return count