from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def rec(ind:int,cur:int)->int:
            if ind>len(cost)-1:
                return cur
            lol = cur + cost[ind]
            return min(rec(ind+1,lol),rec(ind+2,lol))
        return min(rec(0,0),rec(1,0))
        