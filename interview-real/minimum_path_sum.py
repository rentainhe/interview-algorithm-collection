class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        # 定义grid[i][j]存储的是从起始点到(i,j)的最短路径
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 在出发点，不作任何操作
                if i == j == 0:
                    continue
                # 当左边是边界是，只能从上面来
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                # 当上面是边界是，只能从左边来
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                # 当没有遇到边界的时候，最小的值是上面和左边两个点里选一个最小的
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
