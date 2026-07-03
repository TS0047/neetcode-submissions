class Solution:
    def hammingWeight(self, n: int) -> int:
        lol = bin(n)
        count = 0
        for i in str(lol):
            if i == '1':
                count+=1

        return count