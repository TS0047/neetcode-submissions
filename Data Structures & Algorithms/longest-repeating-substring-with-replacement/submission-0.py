class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        bigger = 0
        counts = {}
        for r in range(0,len(s)):
            counts[s[r]] = counts.get(s[r],0)+1
            rep = r-l+1 - max(counts.values())
            while rep>k:
                counts[s[l]]-=1
                l+=1
                rep = r-l+1 - max(counts.values())
            bigger = max(bigger,r-l+1)
        return bigger