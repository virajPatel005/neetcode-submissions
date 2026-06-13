class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


            i=0

            finale=""
            while i<max(len(word1),len(word2)):
                if i==len(word1) :
                    finale+=word2[i:]
                    break
                if i==len(word2):
                    finale+=word1[i:]
                    break

                finale+=word1[i]+word2[i]
                i+=1
            return finale
 


        