class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        lenght =0
        seen = set()
        for j in range(0,len(s)):
            if s[j] in seen:
                while s[j] in seen:
                    seen.remove(s[i])
                    i+=1
            lenght = max(lenght,j-i+1)
            seen.add(s[j])
        return lenght

            