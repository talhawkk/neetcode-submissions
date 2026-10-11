class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        n=int(l/2)
        h={}
        if l==1:
            return nums[0]
        for i in range(l):
            if nums[i] in h:
                h[nums[i]]+=1
                if h[nums[i]]>n:
                    return nums[i]
            if nums[i] not in h:
                h[nums[i]]=1
            
