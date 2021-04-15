from typing import List


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
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])

        backtrack(nums, [])

        return res
