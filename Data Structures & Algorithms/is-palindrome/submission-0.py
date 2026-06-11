class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_li=[i.lower() for i in s if i.isalnum() and i !=" "]
        # ['W', 'a', 's', 'i', 't', 'a', 'c', 'a', 'r', 'o', 'r', 'a', 'c', 'a', 't', 'I', 's', 'a', 'w']
        j=len(s_li)-1
        check_li=[]
        while j>=0:
            check_li.append(s_li[j])
            j-=1
        if check_li==s_li:
            return True
        else:
            return False
        
        