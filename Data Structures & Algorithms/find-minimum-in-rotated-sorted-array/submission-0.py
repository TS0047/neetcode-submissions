class Solution:
    
    def findMin(self, nums: List[int]) -> int:
        self.array = nums
        return self.rec(0,len(nums)-1)
    def rec(self,i:int, j:int)->int:
        if i == j:
            return self.array[i]
        mid = (i+j)//2

        return min(self.rec(i,mid),self.rec(mid+1,j))
