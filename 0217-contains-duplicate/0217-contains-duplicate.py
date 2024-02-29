class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no=set(nums)
        
        if len(nums)==len(no):
            return False 
        
        return True