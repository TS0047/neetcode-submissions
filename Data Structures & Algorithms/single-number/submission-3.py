class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        var = nums[0]
        for i in range(1,len(nums)):
            var = var^nums[i]
        return var