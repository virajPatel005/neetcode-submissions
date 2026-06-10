class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        qualified=len(nums)/3
        from collections import Counter
        count_dict=Counter(nums)
        print(count_dict)
        #Counter({2: 5, 5: 4, 3: 1})
        #for i,j in count_dict.values
        li=[i for i,j in count_dict.items() if j>qualified]
        return li
        