from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # 时刻记住 nums 是可选择列表, path是已选择列表
        def backtrack(nums, path, index):
            # 剪枝, 当当前路径的和大于target的时候, 不考虑之后的结果
            if sum(path) > target:
                return

            if sum(path) == target and path not in res:
                res.append(path)
                return
            # nums 是可选择列表, path 是已选择列表
            # 因为这一题可以选择重复的数字, 所以初始的 nums 列表应该是空的, 在每次选择后把当前的选择添加进可选择列表中
            # 这里需要额外传入一个index参数控制: 因为在 index=0的情况下遍历完得到结果后, 再遍历index=1、index=2...之后的情况
            for i in range(index, n):
                backtrack(nums, path + [candidates[i]], i)

        n = len(candidates)
        backtrack([], [], 0)  # 这里的 nums 根本没用到, 对候选列表没有限制, 只要在范围内就行了
        return res


class SolutionV2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # 这题很特殊的点在于, nums == path, 因为可以选择重复的值, 所以可选列表和已选列表是可以整合成一个列表的
        # 为什么需要设置 index, index是控制找的元素的, 当 index=0 的找完了, 开始找 index=1、index=2...的
        def backtrack(path, index):
            if sum(path) > target:
                return

            if sum(path) == target and path not in res:
                res.append(path)
                return

            for i in range(index, n):
                backtrack(path + [candidates[i]], i)

        n = len(candidates)
        backtrack([], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 3, 7]
    target = 7
    print(s.combinationSum(nums, target))
