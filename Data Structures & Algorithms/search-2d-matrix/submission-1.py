class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        search_matrix = 0
        for i in range(1,m):
            if matrix[i-1][n-1]<target and matrix[i][n-1]>=target:
                search_matrix = i
                break
        if search_matrix==0 and matrix[0][n-1]<target:
            return False
        return self.rec(matrix[search_matrix],target)
        

    def rec(self,matrix :List[int],target:int)->bool:
        size = len(matrix)
        if matrix[0]==target:
            return True
        if size>1:
            partition = int(size/2)
            arr1 = matrix[0:partition]
            arr2 = matrix[partition:size]
            return self.rec(arr1,target) or self.rec(arr2,target)
        else:
            return False


        