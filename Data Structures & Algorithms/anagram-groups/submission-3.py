class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_li = []

        for words in strs:
            li = []

            for chars in words:
                li.append(chars)

            li.sort()

            word = "".join(li)
            word_li.append(word)

        li = {}

        for value in word_li:
            li[value] = []

        for i in range(len(strs)):
            li[word_li[i]].append(strs[i])

        finale = []

        for value in li.values():
            finale.append(value)

        return finale