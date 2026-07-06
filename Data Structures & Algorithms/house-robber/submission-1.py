class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0   # best up to i-2, i-1
        for n in nums:
            prev, cur = cur, max(cur, prev + n)
        return cur