class Solution:

    def encode(self, strs: List[str]) -> str:
        chara = '#'
        self.word = ''

        for i in strs:
            self.word += str(len(i)) + chara + i

        return self.word

    def decode(self, s: str) -> List[str]:
        encoded_strs = s
        i = 0
        decoded_strs = []
        temp = ''

        while i < len(encoded_strs):

            if encoded_strs[i] == "#":

                length = int(temp)
                temp = ''

                word = encoded_strs[i + 1:length + i + 1]
                decoded_strs.append(word)

                i += 1 + length

            else:
                temp += encoded_strs[i]
                i += 1

        return decoded_strs
