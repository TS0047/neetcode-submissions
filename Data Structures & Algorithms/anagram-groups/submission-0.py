class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for i in strs:
            srt = list(i)
            srt.sort()
            if str(srt) in temp:
                temp[str(srt)].append(i)
            else:
                temp[str(srt)] = [i]
        return [j for j in temp.values()]

        
        