class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result , current = [] , []
        lenght = len(nums)
        def rec(i):
            if lenght == i:
                result.append(current[:])
                return

            rec(i+1)
            current.append(nums[i])
            rec(i+1)
            current.pop()
            return
        rec(0)
        return result

            
            
            
            

        
            


        