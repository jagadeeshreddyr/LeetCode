class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        sum1 = 0
        n = len(nums) - 1
        
        nums.sort()
        for i in range(k):
            
            sum1 += nums[n]
            
            nums[n] +=1
            
            
        return sum1