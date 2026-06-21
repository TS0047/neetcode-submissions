class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array = sorted(nums)
        out = []
        for index,i in enumerate(array):
            if index > 0 and array[index] == array[index-1]:
                continue
            wanted = -i
            l,r = index+1,len(array)-1
            while(r>l):
                ans = array[r]+array[l]
                if ans == wanted:
                    out.append([i,array[l],array[r]])
                    r-=1
                    l+=1
                    while l<r and array[l] == array[l-1]:
                        l+=1
                    while l<r and array[r+1] == array[r]:
                        r-=1
                    
                elif ans>wanted:
                    r-=1
                else :
                    l+=1
        return out