class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs)==1:
            pre=strs[0]
        else:

            pre=""
            compare=strs[0]
            for i in range(1,len(strs)):
                for j in range(1,len(compare)+1):
                    print(strs[i][:j])
                    print(compare[:j])
                    if strs[i][:j]==compare[:j]:
                        pre=strs[i][:j]
                    else:
                        break
                compare=pre
        return pre

        


            
        