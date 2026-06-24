from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def rec(n):
            if n < 1: return 0
            if n <= 2: return n
            return rec(n-1) + rec(n-2)
        return rec(n)