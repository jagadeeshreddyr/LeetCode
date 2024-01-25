class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values=dict()
        
        for i, elem in enumerate(nums):
            
            comp=target-elem 
    
            if comp in values:
        
                return [values[comp],i]
        
            values[elem]=i
            
        return []