class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]

        count=0
        for i,n in enumerate(nums):
                diff=target-n
                
                if diff in nums[i+1:]:
                    output.append(i)
                    index=nums[i+1:].index(diff)
                    original_index=index+len(nums[:i+1])
                    output.append(original_index)
                    return output
               



        


        