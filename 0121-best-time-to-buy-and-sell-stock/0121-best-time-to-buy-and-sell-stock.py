class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lw = prices[0]
        mi = []
        
        for i in range(0, len(prices)):
            if prices[i] <lw:
                lw = prices[i]
            mi.append(lw)
    
        hi = prices[-1]
        mx = []

        for j in range(len(prices)-1,-1,-1):

            if prices[j] >hi:
                hi = prices[j]

            mx.append(hi)
    
    
        mx.reverse()

        st = []
        for i in range(len(mi)):


            st.append(mx[i] - mi[i])

        return max(st)