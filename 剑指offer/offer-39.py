from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 寻找众数: 暴力求解, 使用hashmap来存每个nums出现的次数
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        for i in hashmap.keys():
            if hashmap[i] > len(nums) // 2:
                return i
