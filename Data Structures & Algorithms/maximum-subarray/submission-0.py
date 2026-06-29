class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None :
            return 0
        cur = nums[0]
        bigger = nums[0]
        for i in range(1,len(nums)):
            cur = max(nums[i],cur+nums[i])
            bigger = max(bigger,cur)
        return bigger