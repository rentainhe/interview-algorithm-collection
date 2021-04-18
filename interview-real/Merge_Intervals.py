"""
合并区间
https://leetcode-cn.com/problems/merge-intervals/
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 处理特殊情况
        if len(intervals) == 0:
            return []

        res = []
        intervals.sort(key=lambda x: x[0])  # 关键步骤是, 一定要按照左区间进行排序
        for inter in intervals:
            # res[-1][-1] 表示结果集的最后一个元素的右区间, inter[0]表示新加入的区间的左区间, 如果右小于左, 则代表这是一个新的区间, 需要添加进来
            if len(res) == 0 or res[-1][-1] < inter[0]:
                res.append(inter)
            else:
                res[-1][-1] = max(res[-1][-1], inter[1])  # 合并右区间, 如果新添加的区间的右区间更大的话, 则选择更大的那个
        return res
