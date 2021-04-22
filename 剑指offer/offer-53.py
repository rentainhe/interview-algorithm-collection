from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 当对应 index 的数不等于 index 的时候, 直接返回 index 的值
        for index, num in enumerate(nums):
            if index != num:
                return index
        # 如果 0 ~ n-1 都在数组里, 那么只有 n 不在, 所以 return len(nums)
        return len(nums)