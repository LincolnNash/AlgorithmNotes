class Solution(object):
    #深度优先遍历
    def dfs_rec(self,grid, r, c):
        grid[r][c] == "0"
        nr = len(grid)
        nc = len(grid[0])
        for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0<=x<nr and 0<=y<nc and grid[x][y]=="1":
                self.dfs_rec(grid, x, y)
    #深度优先遍历（迭代）
    def dfs_iter(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        stack=[(r,c)]
        while len(stack)>0:
            x, y = stack.pop()
            grid[x][y] = "0"
            for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= dx < nr and 0 <= dy < nc and grid[dx][dy] == "1":
                    stack.append((dx, dy))


    #岛屿数量
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr = len(grid)
        if len(grid) == 0:
            return 0
        nc = len(grid[0])
        num_island = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_island+=1
                    self.dfs_iter(grid,r,c)
        return num_island
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s = Solution()
print(s.numIslands(grid))
