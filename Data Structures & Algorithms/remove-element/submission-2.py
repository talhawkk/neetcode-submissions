class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l=len(nums)
        num=[]
        num=list(nums)

        for i in range(l):
            if num[i]==val:
                nums.remove(val)
        l=len(nums)
        return l