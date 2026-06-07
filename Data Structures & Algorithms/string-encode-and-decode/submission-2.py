class Solution:

    def encode(self, strs: List[str]) -> str:
        self.encoded_word=""
        char="#"
        for i in strs:
            self.encoded_word+=str(len(i))+char+i
        return self.encoded_word
        

    def decode(self, s: str) -> List[str]:
        encoded_word=s
        li=[]
        temp=""
        i=0
        while i<len(encoded_word):
            if encoded_word[i]=="#":
                length=int(temp)
                word=encoded_word[i+1:length+i+1]
                li.append(word)
                i+=length+1
                temp=""
            else:
                temp+=encoded_word[i]
                i+=1
        return li
        
