class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 用 dp[i][j] 来表示从原点到 dp[i][j] 的路径总数
        # init dp array, 初始化状态转移方程的时候必须为 1
        dp = [ [1] * n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                # 当 i 和 j 都等于 0 的时候, 都是只有一条路径
                if i == 0:
                    continue
                elif j == 0:
                    continue
                else:
                    # (i, j) 点的路径是 (i-1, j) 和 (i, j-1) 之和
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
