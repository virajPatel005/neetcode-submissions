class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        li=[]
        while i<len(nums):
            sli=nums[:i]+nums[i+1:]
            pro=1
            for j in sli:
                pro*=j
            li.append(pro)
            i+=1
        return li

