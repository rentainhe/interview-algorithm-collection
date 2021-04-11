class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b  # 内存和计算不会重复
        return a % 1000000007


from functools import lru_cache


class Solution:
    @lru_cache(None)  # 清除缓存工具
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return (self.fib(n - 1) + self.fib(n - 2)) % 1000000007


def fib(n):
    hashmap = {}
    hashmap[0] = 0
    hashmap[1] = 1
    mod = 10 ** 9 + 7

    def helper(n):
        if n < 2:
            return n
        if n in hashmap:
            return hashmap[n]
        else:
            result = helper(n - 1) + helper(n - 2)
            hashmap[n] = result
            return result

    return helper(n) % mod


print(fib(8))
