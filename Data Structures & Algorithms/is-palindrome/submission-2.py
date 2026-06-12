class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_li=[i.lower() for i in s if i.isalnum() and i !=" "]
        i=0
        j=len(s_li)-1
        flag=True

        while i<j:
            if s_li[i]==s_li[j]:
                flag=True
            else:
                flag=False
                break
            i+=1
            j-=1
        if flag==True:
            return True
        else:
            return False

        