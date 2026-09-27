class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        b=False
        for i in nums:
            if i not in d:
                d[i]=0
            elif i  in d:
                b=True
                return b

        return b
