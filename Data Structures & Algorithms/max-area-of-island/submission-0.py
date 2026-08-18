class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.temp = 0
        self.maximal = 0
    
        def cover_land(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return 
            if grid[i][j]==1:
                self.temp+=1
                direction = [[0,1],[0,-1],[1,0],[-1,0]]
                grid[i][j]=0
                for m,n in  direction:
                    cover_land(m+i,n+j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    self.temp = 0
                    cover_land(i,j)
                    print(self.temp," and ",self.maximal)
                    self.maximal = max(self.temp,self.maximal)

        return self.maximal

