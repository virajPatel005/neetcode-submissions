class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        res=max(di,key=di.get)
        return res
        