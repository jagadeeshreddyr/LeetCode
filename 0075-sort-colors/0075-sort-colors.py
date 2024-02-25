class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        low, mid , high, = 0,0, n-1



        while mid <=high:

            if nums[mid] == 0:
                swap = nums[low]
                nums[low] = nums[mid]
                nums[mid] = swap
                low +=1
                mid +=1
            elif nums[mid] ==1:
                mid +=1

            else:
                swap = nums[high]
                nums[high] = nums[mid]
                nums[mid] = swap
                high -=1
                
        return nums