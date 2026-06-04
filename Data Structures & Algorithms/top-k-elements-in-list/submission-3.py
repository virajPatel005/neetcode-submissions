class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count_dict=Counter(nums)
        sorted_dict=sorted(count_dict.items(),key=lambda item:item[1],reverse=True)
        li=list(i[0] for i in sorted_dict)[:k]
        return li