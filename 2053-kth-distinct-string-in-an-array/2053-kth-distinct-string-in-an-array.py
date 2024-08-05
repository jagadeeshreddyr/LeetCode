class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        d = {}
        
        for i in arr:



            if i not in d:
                d[i] = 1

                

            else:


                d[i]+=1
        
        dist = [string for string in arr if d[string] == 1]


        if k <= len(dist):
            return dist[k - 1]

        else:
            return ""