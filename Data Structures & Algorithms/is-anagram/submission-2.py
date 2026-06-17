class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(t)
        if len(s)!=len(t):
            return False
        for i in s:
            if i in a:
                a.remove(i)
            else:
                return False
        return not bool(a)
            

        
        