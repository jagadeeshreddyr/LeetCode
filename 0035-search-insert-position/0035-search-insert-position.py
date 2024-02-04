class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        poi=0
        
        for i in range(len(nums)):
            
            if nums[i]<target:
                poi=i+1
    
        
        return poi