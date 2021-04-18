# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 个人思路是: 构建 hashmap, 然后对 hashmap 的 value 进行排序, 找到排序前 k 个 key 就行了
        # 构建 hashmap
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        # 对 hashmap 的 values 进行排序
        hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)  # reverse = True表示按照降序排列
        # 这里返回的 hashmap 经过 sorted 函数后变成一个 list, 其中每一个元素都是一个元组 (key, value)
        res = []
        for i in range(k):
            res.append(hashmap[i][0])
        return res
