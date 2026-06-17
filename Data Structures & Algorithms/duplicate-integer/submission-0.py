class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = [[] for _ in range(0,10)]
        for i in nums:
            mod = i%10
            num_list = array[mod]
            if i in num_list:
                return True
            array[mod].append(i)
        return False


        