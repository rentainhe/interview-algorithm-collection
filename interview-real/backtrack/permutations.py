from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path):  # nums表示可选列表，path表示路径，也就是已选择的列表
            if not nums:  # 满足结束条件，nums中没有选择，将已选择好的path添加进result列表中
                res.append(path)
                return
            for i in range(len(nums)):  # 每次从一个点开始选择
                # nums[:i] + nums[i+1:] 表示新的选择列表
                # path + [num[i]] 这是已选择的列表
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        backtrack(nums, [])
        return res