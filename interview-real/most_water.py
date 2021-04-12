from typing import List


# 定义左右指针，每次向内移动短指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height) - 1
        i = 0
        s = 0
        while i < j:
            tmp = min(height[i], height[j]) * (j - i)
            if tmp > s:
                s = tmp
            if height[i] < height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
        return s


# 更优雅的写法
class SolutionV2:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
