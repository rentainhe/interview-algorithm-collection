from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 状态定义: nums[i] 表示以 nums[i] 为结尾的最大连续数组和
        # 当 nums[i-1] < 0 的时候, 此时 nums[i-1] + nums[i] 还不如 nums[i] 本身
        # 初始化的时候 nums[o] = nums[0]

        # 写法1
        # for i in range(1, len(nums)):
        #     nums[i] += max(nums[i - 1], 0)
        # return max(nums)

        # 写法2
        # init dp
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] < 0:  # 当 dp[i-1]小于0的时候, 此时dp[i]的结果就是nums[i], 因为之前的数为0, 加上后为负收益, 所以不需要加
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)
