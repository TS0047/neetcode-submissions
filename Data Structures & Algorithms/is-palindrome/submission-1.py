class Solution:
    def isPalindrome(self, s: str) -> bool:
        bol = []
        for i in s.lower():
            if i.isalpha() or i.isdigit():
                bol.append(i)
        lol = bol[:]
        lol.reverse()
        if lol == bol:
            return True
        return False
