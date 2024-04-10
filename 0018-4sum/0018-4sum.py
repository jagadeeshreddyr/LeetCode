class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        rr=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                t=target-nums[i]-nums[j]
                l=j+1
                r=len(nums)-1
                while(l<r):
                   
                    if nums[l]+nums[r]>t:
                        r=r-1
                    elif nums[l]+nums[r]<t:
                        l=l+1
                    else:
                        q=[nums[i],nums[j],nums[l],nums[r]]
                        # print(q)
                        if q not in rr:
                            rr.append(q)
                        while(l<r and nums[l]==q[2]):
                            l=l+1
                        while(l<r and nums[r]==q[2]):
                            r=r-1
                while(j+1<len(nums) and nums[j+1]==nums[j]):
                    j=j+1
        while(i+1<len(nums) and nums[i+1]==nums[i]):
                    i=i+1
        return rr