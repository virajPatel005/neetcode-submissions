class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [[strs[0]]]
        word_li=[]

        for words in strs:
            li=[]
            for chars in words:
                li.append(chars)
            li.sort()
            word_li.append(li)
        index_li=[]
        index_dic={}
        for num,value in enumerate(word_li):
            values="".join(value)
            if values in index_dic:
                index_dic[values].append(num)
            else:
                
             index_dic[values]=[num]
        finale_li=[]
        for value in index_dic.values():
            li=[]
            for index in value:
                li.append(strs[index])
            finale_li.append(li)
        return finale_li
                            
            
        