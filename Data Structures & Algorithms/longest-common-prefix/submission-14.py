class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return  strs[0]
        

        ref=strs[0]
        
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if   i==len(word) or word[i]!=ref[i]:
                    return ref[:i]
                    
        return ref