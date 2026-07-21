class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.arr = []
        nums.sort()

        def rec(ind: int):
            if ind == len(nums):
                self.answer.append(list(self.arr))
                return

            self.arr.append(nums[ind])
            rec(ind + 1)
            self.arr.pop()
            if len(self.arr) == 0 or self.arr[-1] != nums[ind]:
                rec(ind + 1)

        rec(0)
        return self.answer
