from typing import List

# 排除重复情况
# 这里的解法是一种naive version, 因为用了 if not in 这种写法, 感觉并不会提速
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []

        res = []

        def backtrack(nums, path):
            if not nums:
                if path not in res:
                    res.append(path)
                return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])

        backtrack(nums, [])

        return res