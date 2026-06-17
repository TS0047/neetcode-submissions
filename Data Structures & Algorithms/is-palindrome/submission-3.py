class Solution:
    def isPalindrome(self, s: str) -> bool:
        lol = list(s.lower())
        i,j=0,len(lol)-1
        while(i<j):
            if not (lol[i].isalpha() or lol[i].isdigit()):
                i+=1
                continue
            if not (lol[j].isalpha() or lol[j].isdigit()):
                j-=1
                continue
            if lol[i]!=lol[j]:
                return False

            i,j = i+1,j-1
        return True
        