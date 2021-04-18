"""
leetcode 70
https://leetcode-cn.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 本质上就是斐波那契数列问题
        # 第n层的走法是第n-1层和第n-2层的和
        if n == 1:
            return 1
        elif n == 2:
            return 2
        # 初始化 dp 列表, dp列表中每个位置代表走到第 n 层楼梯的走法
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        # 进行 dp 操作
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
