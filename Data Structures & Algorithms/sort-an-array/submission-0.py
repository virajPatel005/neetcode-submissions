class Solution:

    def merge_arr(self,left,right):
        
        n,m=len(left),len(right)
        i,j=0,0
        li=[]
        while i<n and j<m:
            if left[i]<right[j]:
                li.append(left[i])
                i+=1
            else:
                li.append(right[j])
                j+=1
        if i==n:
            li.extend(right[j:])
        if j==m:
            li.extend(left[i:])
        return li


    def sortArray(self, nums: List[int]) -> List[int]:
        mid=len(nums)//2
        if len(nums)<=1:
            return nums

        left_arr=nums[:mid]
        right_arr=nums[mid:]
        left=self.sortArray(left_arr)
        right=self.sortArray(right_arr)

        return self.merge_arr(left,right)




        