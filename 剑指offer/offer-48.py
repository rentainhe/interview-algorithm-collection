# encoding: utf-8
# 最长不含重复字符的子字符串: 快慢指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        max_len = 0
        while fast < len(s):
            # 快指针遍历一遍数组
            # 当快指针遍历到重复的位置时, 移动慢指针直到数组里没有重复的元素
            while s[fast] in s[slow:fast]:  # s[2:2] = ''
                slow += 1
            if fast - slow + 1 > max_len:
                max_len = fast - slow + 1
            # 进行完一次判断后快指针移动一位
            fast += 1
        return max_len