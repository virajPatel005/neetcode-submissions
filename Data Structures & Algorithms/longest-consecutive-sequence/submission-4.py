class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        num_set=set(nums)
        ans=set()
        max_length=0
        for i in num_set:
            if i-1 not in num_set:
                current=i
                length=1
                while current+1 in num_set:
                    
                        current+=1
                        length+=1
                else:
                    if length>max_length:
                        max_length=length
        return max_length
        

    
        
    





        