from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, k):
            # i, j 表示遍历到的元素, k 对应 word 上 str 的index
            # 使用 dfs 算法, 添加剪枝条件
            # 当数组下标越界的时候, 以及新添加的元素(i,j)不等于word中对应的index为k的元素时
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            # 当添加的元素恰好为word中最后一个元素时, 说明找到了
            if k == len(word) - 1: return True
            # 走到这一步说明, board[i][j] == word[k]
            board[i][j] = ''  # 让 board[i][j] = '' 是为了防止再次选择自身
            # 每次可选的位置有, 右, 左, 下, 上
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]  # 当找完从 (i, j) 这个点开始的所有元素后, 要记得恢复 board[i][j]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
