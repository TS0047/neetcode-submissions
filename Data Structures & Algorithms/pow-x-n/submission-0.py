class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        num = x
        ans = float(1)
        if n <0 : 
            num = 1/num
        for i in range(0,power):
            ans*=num
        return ans
        