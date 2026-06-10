class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:



        prefix=[0 for i in range(len(nums))]
        # [0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(0,len(nums)):
            if i==0:
                prefix[i]=nums[i]
            else:
                prefix[i]=nums[i]+prefix[i-1]
        # [3, 7, 14, 16, 13, 14, 18, 20]
        num_dict={0:1}
        count=0
        for i in prefix:
            if i-k in num_dict:
                count+=num_dict[i-k]
            num_dict[i]=num_dict.get(i,0) +1
        return count
        