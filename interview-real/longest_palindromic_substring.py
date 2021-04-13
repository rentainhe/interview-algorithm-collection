# encoding: utf-8

# 中心拓展法
class SolutionV1:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 当字符串长度小于2时直接返回
        if n < 2:
            return s

        # 中心拓展
        def center_spread(L: int, R: int) -> str:
            while 0 <= L and R < n and s[L] == s[R]:
                L -= 1
                R += 1
            return s[L + 1:R]  # 这一步 L+1很关键, 可以排除 abc 这种情况

        # 例如传入的L=1, R=1, 最后return的值是 s[1,2] 也就是s[1]这个字符
        res = s[0]
        max_len = 1
        # 遍历获得结果
        for i in range(n):
            # 得到奇数情况下最长的str和偶数情况下最长的str
            odd_str = center_spread(i, i)
            even_str = center_spread(i, i + 1)
            # 分别进行比较
            if len(odd_str) > len(even_str):
                if len(odd_str) > max_len:
                    max_len = len(odd_str)
                    res = odd_str
            else:
                if len(even_str) > max_len:
                    max_len = len(even_str)
                    res = even_str
        return res


# 动态规划: 首先假设dp[i][j]表示i到j的字符串是不是回文子串
# dp[i][j]为回文子串的条件是, dp[i][j]中 s[i]==s[j] 并且 s[i+1]==s[j-1]
# 如果 s[i]==s[j], 则dp[i][j] == dp[i+1][j-1]
# 每次更新完dp[i][j]后, 更新 max_len 和 start
# 边界: len(s) < 2时必为回文串, dp[i][i]=True

class SolutionV2:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划, dp[i][j]表示s[i:j]是否为回文子串
        # 每次判断 s[i][j]的时候更新 max_len = j-i+1 和 start = i
        # 边界, 当 j-i+1<2 的时候肯定是回文串, 也就是说 j<i+1 的时候, 也就是 j == i 的时候
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        # 边界
        if n < 2:
            return s

        # dp初始化
        for i in range(n):
            dp[i][i] = True

        # 枚举区间终点
        for R in range(1, n):
            for L in range(0, R):
                if s[L] == s[R]:
                    if R - L < 3:  # R - L <= 3的时候已经包含了 aa 这种偶数情况
                        dp[L][R] = True
                    else:
                        dp[L][R] = dp[L + 1][R - 1]  # 当 s[L] == s[R] 时, dp[L][R] = dp[L+1][R+1]

                if dp[L][R]:
                    length = R - L + 1
                    if length > max_len:
                        max_len = length
                        start = L

        return s[start: start + max_len]
