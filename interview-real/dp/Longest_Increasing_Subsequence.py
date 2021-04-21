from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # init dp
        # 假设 dp[i] 为以 nums[i] 结尾的最长递增子序列
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    # 当 nums[i] 大于 nums[j] 的时候
                    # 即 当前元素 比 之前的某个元素 大, 所以要么是当前元素的最大值, 要么是之前那个元素的最大长度+1（包括进来当前元素后长度会+1）
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)