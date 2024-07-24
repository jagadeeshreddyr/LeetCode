class Solution:
    def pivotInteger(self, n: int) -> int:
        
        
        f1 = [x for x in range(1, n+1)]

        c = 1
        while c<=n:


            if sum(f1[c-1:]) == sum(f1[:c]):

                return c

            c+=1

        return -1