class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lol = {}
        for i in nums:
            if i in lol:
                lol[i]+=1
            else :
                lol[i] = 0
        sorted_dict =dict(sorted(lol.items(), key = lambda item : item[1]))
        output = []
        l = len(list(sorted_dict.items()))-1
        for j in range(0,k):
            output.append(list(sorted_dict.items())[l][0])
            l-=1
        return output

        