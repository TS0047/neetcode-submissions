class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if self.rec_search(nums,target):
            return nums.index(target)
        return -1
    
    def rec_search(self,array:List[int],target:int)->int:
        if array[0]==target:
            return True
        size = len(array)
        if size>1:
            partition = int(size/2)
            arr1 = array[0:partition]
            arr2 = array[partition:size]
            return self.rec_search(arr1,target) or self.rec_search(arr2,target)

