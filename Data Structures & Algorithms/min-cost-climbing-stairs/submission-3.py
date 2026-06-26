class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totals = [0] * len(cost)
        totals[0] = cost[0]
        totals[1] = cost[1]
        for i in range(2, len(cost)):
            totals[i] = min(totals[i - 1] + cost[i], totals[i - 2] + cost[i])
        return min(totals[-2:])