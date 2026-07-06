class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_hash = {}
        last_index = len(cost)-1 
        cost_hash[last_index],cost_hash[last_index+1] = cost[last_index],0
        for i in range(last_index-1,-1,-1):
            cost_hash[i] = min(cost_hash[i+1],cost_hash[i+2])+cost[i]
        return min(cost_hash[1],cost_hash[0])

            


            
