from typing import List


# 重点需要考虑的是重复的情况, 如果是aab, 则全部的可能输出为 aba baa aab

class Solution:
    def permutation(self, s: str) -> List[str]:
        # 对字符串进行排序是为了能够更好地判断是否有考虑重复元素
        s = sorted(list(s))
        res = []

        def dfs(s, road):
            if s == []:
                res.append(''.join(road))
            for i in range(len(s)):
                # 剪枝操作, 当当前元素和前一个元素相同的时候, 全遍历会产生同样的结果, 所以这一步需要剪枝掉
                if i > 0 and s[i] == s[i - 1]: continue
                dfs(s[:i] + s[i + 1:], road + [s[i]])

        dfs(s, [])
        return res
