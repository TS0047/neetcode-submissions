class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        size = len(nums)
        
        def rec(i:int,sum:int):
            if i == size or sum>target:
                return 
            if sum == target:
                res.append(cur[:])
                return
            cur.append(nums[i])
            rec(i,sum+nums[i])
            cur.pop()
            rec(i+1,sum)
        rec(0,0)
        return res
