class Solution:



    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1



        def check(a,b):
           
            while a<b:
                if s[a] != s[b]:
                    return False
                    break
            
                a+=1
                b-=1
            return True

        while i<j:
    
            if s[i].lower() != s[j].lower():
                
               return  check(i+1,j) or check(i,j-1)
                
        
    
            i+=1
            j-=1

        return True

        

    



        