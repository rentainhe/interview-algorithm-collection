"""
https://leetcode-cn.com/problems/jump-game-ii/
跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每一个元素表示你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

例如 [2,3,1,1,4]
return 2
跳到最后一个位置, 只需要先跳到第二个位置, 再从第二个位置跳到最后一个位置即可
"""

class Solution(object):
    def jump(self, nums):
        # init dp
        # 定义 dp[i] 表示从数组第一个位置跳到第i个位置所需要的最少跳跃次数
        # 默认情况下跳到每一个的至少都要经过之前的格子, 所以每个位置初始化为对应的index
        res = [i for i in range(len(nums))]
        for i in range(len(nums)):
            # temp = i（现在的位置坐标）+ nums[i] （能飞的最大距离）
            temp = i + nums[i]  # 其所能到的所有格子下标
            # 每到一个格子, 都要更新一下它所能到的所有格子的下标, 如果比原来的少, 则更新
            for j in range(i, temp + 1):
                if j < len(nums):
                    res[j] = min(res[j], res[i] + 1)
        return res[-1]
