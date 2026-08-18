class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        count = 0
        def clear_island(i,j):
            if i>=len(grid) or i < 0 or j >= len(grid[0]) or j <0:
                return
            if (i,j) in self.visited:
                return
            if grid[i][j]=="1":
                self.visited.add((i,j))
                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                for k,m in directions:
                    clear_island(i+k,j+m)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and  (i,j )not in self.visited:
                    count +=1
                    clear_island(i,j)
        return count
        