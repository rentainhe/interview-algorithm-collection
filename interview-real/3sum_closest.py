# encoding: utf-8
from typing import List


# 最接近 target 的三数之和, 排序+双指针
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 先初始化一个result, 为前三个数之和, 为了涵盖list大小只有3的情况
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        n = len(nums)
        # 从数组最左边开始遍历
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(target - s) < abs(target - res):
                    res = s
                if s < target:  # 当s比target小的时候, 移动左指针, 让s变大, 有可能得到更优解
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return res
        return res
