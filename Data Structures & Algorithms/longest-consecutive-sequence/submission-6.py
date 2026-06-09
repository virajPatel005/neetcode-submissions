class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        num_set=set(nums)
        max_length=0

        if len(num_set)==1:
            return 1
        if not num_set:
            return 0
        for i in num_set:
            if i-1 not in num_set:
                current=i
                length=1
                while current+1 in num_set:
                    
                        current+=1
                        length+=1
                if length>max_length:
                        max_length=length
        return max_length
        

    
        
    





        