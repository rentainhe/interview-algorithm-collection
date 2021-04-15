from typing import List

"""
        例1:
                  1
                 / \
                2   2  这种情况不会发生 
               /     \
              5       5
        例2
                  1
                 /
                2      这种情况确是允许的
               /
              2  
"""


# 可以允许数重复出现在一个case里, 但不允许一个case重复
# 可以允许不同级出现相同的元素, 但是不允许同一级出现相同的元素
# 判断 candidates[i] == candidates[i-1] 就可以砍掉第一种情况
# 在一个 for 循环中, 所有被遍历到的数都是属于同一级的
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(candidatas, path):
            if sum(path) > target: return
            if sum(path) == target:
                res.append(path)
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(candidates[i + 1:], path + [candidates[i]])

        backtrack(candidates, [])
        return res

