class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.arr = []
        def rec(rem:list):
            if len(self.arr)==len(nums):
                self.answer.append(list(self.arr))
                return 
            
            for i in rem:
                temp = list(rem)
                temp.remove(i)
                self.arr.append(i)
                rec(temp)
                self.arr.remove(i)

        rec(nums)
        return self.answer




        