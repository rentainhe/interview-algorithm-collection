# encoding: utf-8
from typing import List


# 对于排序的数组, 查找元素, 使用二分查找速度比较快
# 常规二分查找代码如下:
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
            return mid  # 在这题的背景下, 只需要修改当查找到对应index的时候的操作
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找，搜索左右边界
        if not nums:
            return [-1, -1]
        return [self._search_left(nums, target), self._search_right(nums, target)]

    def _search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1  # 改动这里，使搜索区间向左侧收缩
        if left >= len(nums) or nums[left] != target:  # 判断索引越界情况
            return -1
        return left

    def _search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1  # 改动这里，使搜索区间向右侧收缩
        if right < 0 or nums[right] != target:  # 判断索引越界情况
            return -1
        return right
