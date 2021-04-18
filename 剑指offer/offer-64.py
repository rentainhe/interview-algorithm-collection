# encoding: utf-8

class Solution:
    def sumNums(self, n: int) -> int:
        mid = n // 2
        if n % 2 == 0:  # 判断奇数偶数
            return n * mid + mid
        else:
            return n * mid + n
