class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        nums_dict=Counter(nums)

        li=[[] for i in range(len(nums)+1)]
        #li=[[], [], [], [], [], [], [], [], [], []]
        for i,j in nums_dict.items():
            li[j].append(i)
        #print(li)
        #li=[[], [4], [1], [5], [], [], [], [], [], []]
        count=0
        result=[]
        for i in li[::-1]:
            if i:
                for j in i:
                    result.append(j)
                    count+=1
                if count==k:
                    break
        return result

        