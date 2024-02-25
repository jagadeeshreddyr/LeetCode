class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        minimal = prices[0]
        profit = 0


        for n in prices:

            if minimal > n:
                minimal = n

            sub = n - minimal

            if sub > profit:
                profit = sub 
                
        return profit