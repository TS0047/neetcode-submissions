class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        size = len(nums)
        nums.sort()
        
        def rec(i:int,sum:int):
            if sum == target:
                res.append(cur[:]);return
            if i == size or sum>target:
                return 
            cur.append(nums[i])
            rec(i+1,sum+nums[i])
            cur.pop()
            j=i+1
            while j<size and nums[j]==nums[i]:
                j+=1
            rec(j,sum)
        rec(0,0)
        return res
