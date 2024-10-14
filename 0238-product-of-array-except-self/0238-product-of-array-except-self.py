class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        
        answer = [1] * len(nums)
        
        
        left_product = 1 
        
        for left in range(len(nums)):
            
            answer[left] = left_product
            
            left_product *= nums[left]
            
            
        right_product = 1 
        
        for right in range(len(nums)-1,-1, -1):
            
            answer[right] *= right_product
            
            right_product *= nums[right]
            
            
        return answer
            
            
        
        