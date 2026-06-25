class Solution:
    def isHappy(self, n: int) -> bool:
        def num(s:str)->int:
            res = 0
            for i in s:
                res+= int(i)*int(i)
            return res
        temp = n
        seen = set()
        while True:
            temp = num(str(temp))
            if temp == 1:
                return True
            if temp in seen:
                return False
            seen.add(temp)
        return False
        