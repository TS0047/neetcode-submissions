class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind = {}
        for index,i in enumerate(numbers):
            res = target-i
            if res in ind:
                return [ind[res]+1,index+1]
            else:
                ind[i]=index
            

        