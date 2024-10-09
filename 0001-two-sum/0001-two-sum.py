class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        n = len(nums)
        
        
        i = 0
        
        j = 1
        
        
        while j<n:
            
            
            if nums[i]+nums[j] == target:
                
                return [i,j]
            
            j+=1
            
            
            if j==n:
                
                i+=1
                j= i+1
                
                
                
                