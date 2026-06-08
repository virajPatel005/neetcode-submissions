class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp=[1 for i in range(len(nums))]
        #temp=[1, 1, 1, 1, 1]
        left=[1 for i in range (len(nums))]
        for i in range(1,len(left)):
            left[i]=left[i-1]*nums[i-1]
        right=[1 for i in range (len(nums))]
        for i in range(len(right)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        li=[]
        for i in range(len(nums)):
            pro=left[i]*right[i]
            li.append(pro)
        return li
            
    
        

        