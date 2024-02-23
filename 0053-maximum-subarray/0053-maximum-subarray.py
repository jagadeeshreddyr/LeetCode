class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        sum1 = 0
        max1 = float('-inf')  # Initialize max1 to negative infinity

        st = 0
        ed = 0

        for ind, val in enumerate(nums):
            sum1 += nums[ind]

            if sum1 > max1:
                max1 = sum1
                st = ed  # Update start index of maximum sum subarray
                en = ind  # Update end index of maximum sum subarray

            if sum1 < 0:
                sum1 = 0
                ed = ind + 1 
                
                
        return max1