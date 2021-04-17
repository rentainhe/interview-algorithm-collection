from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 定义 dp[i][j] 为走到 (i, j) 这个点能得到的最大礼物数量
        # 直接在原数组上进行操作就行了
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:  # 初始节点就是本身
                    continue
                elif i == 0:  # 当在棋盘的最上面时, 只能从左边来
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  # 当在棋盘的最左边时, 只能从上边来
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:  # 其他时间需要判断, (i-1, j) 和 (i, j-1) 哪个数量多
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
