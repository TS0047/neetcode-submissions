class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        for j in range(1,len(prices)):
            if prices[j]<prices[i]:
                    i = j
            profit = max(profit,prices[j]-prices[i])
        return profit

