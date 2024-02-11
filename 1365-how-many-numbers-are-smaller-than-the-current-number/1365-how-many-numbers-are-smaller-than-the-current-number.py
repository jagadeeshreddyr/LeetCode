class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        s=[]
        #s=nums
        res=0
        n=len(nums)
        
        for i in range(0,n):
            res=0
            for j in range(0,n):
                if nums[i]>nums[j]:
                    res+=1
            s.append(res)
                    
        return s 