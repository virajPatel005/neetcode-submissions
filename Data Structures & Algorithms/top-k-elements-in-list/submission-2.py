class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import itertools
        count_dict=Counter(nums)
        sorted_dict=dict(sorted(count_dict.items(),key=lambda item:item[1],reverse=True))
        li=list(sorted_dict.keys())[:k]
        return li


        