class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            lol = bin(i)
            count = 0
            for j in str(lol):
                if j == '1':
                    count+=1
            out.append(count)
        return out