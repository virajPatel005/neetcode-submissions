class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count=0
        while True:
            
            i,j=0,1
            while i<len(nums) and j<len(nums):
                if nums[j] < nums[i]:
                    temp=nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                i+=1
                j+=1
            count+=1
            if count==len(nums):
                break




        