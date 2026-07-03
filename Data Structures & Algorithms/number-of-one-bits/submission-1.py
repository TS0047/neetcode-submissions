class Solution:
    def hammingWeight(self, n: int) -> int:
        lol = bin(n)
        out= 0
        for i in str(lol)[2:]:
            out+=int(i)
        return out