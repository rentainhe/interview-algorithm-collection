from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 初始化全为 0 的 dp 矩阵, 为什么是 0 呢, 因为要考虑到有障碍物, 障碍物存在会导致路径不通, 不通的情况下默认设置为 0
        temp = [[0] * n for _ in range(m)]
        # 分别对行和列进行初始化
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                temp[0][j] = 1
            else:
                break
        # 等于 0 表示可以到达, 设置为 1
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                temp[i][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                # 只有当 0 的时候可以通行, 才有这种等价公式, 等于 1 的时候不能通行, 还是设置为 0
                if obstacleGrid[i][j] == 0:
                    temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
        return temp[-1][-1]
