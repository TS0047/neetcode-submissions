class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not bool(nums):
            return 0
        j = 0
        out = 1
        lol = list(set(nums))
        lol.sort()
        i=0
        for i in range(1,len(lol)):
            if(lol[i]-lol[i-1]!=1):
                out = max(out,i-j)
                j=i
        out = max(out,i-j+1)
        return out

