class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in nums:
            if i == 0:
                pass
            else:
                prod *=i
        
        output = []
        lol = 0
        for i in nums:
            if i == 0:
                if nums.count(0)>1:
                    lol=0
                else:
                    lol=prod
            else:
                if nums.count(0) == 0:
                    lol=int(prod/i)
                else:
                    lol=0
            output.append(lol)
        return output     