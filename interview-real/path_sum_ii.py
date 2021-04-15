# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
from typing import List

# 注意题目的要求是, 根节点 到 叶子节点 的路径总和
class Solution:  # BFS
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # BFS算法, 需要搭配队列使用, 每次遍历完这个节点后将其子节点加入队列中
        res = []
        que = deque()
        que.append((root, [], 0))  # 将要处理的节点, 路径, 路径和
        while que:
            node, path, pathSum = que.popleft()
            if not node:  # 如果是空节点, 不处理
                continue
            if not node.left and not node.right:  # 因为题目中要求的是叶子节点, 所以这里要判断叶子节点
                if node.val + pathSum == sum:  # 加上叶子节点后，路径和等于sum
                    res.append(path + [node.val])
            que.append((node.left, path + [node.val], pathSum + node.val))
            que.append((node.right, path + [node.val], pathSum + node.val))
        return res

class SolutionV2:  # DFS
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.sum = sum
        res = []
        self.dfs(root, 0, res, [])
        return res

    def dfs(self, root, sum, res, path):
        if not root:  # 空节点, 不做任何处理
            return
        if not root.left and not root.right:  # 遇到叶子节点, 判断求和是否为 sum
            if sum + root.val == self.sum:
                res.append(path+[root.val])
        self.dfs(root.left, sum + root.val, res, path + [root.val])  # 左子树
        self.dfs(root.right, sum + root.val, res, path + [root.val])  # 右子树

if __name__ == "__main__":
    a = deque()  # 提供了pop left的方法
    a.append(1)
    a.append(2)
    a.append(3)
    a.popleft()  # 从左边移出元素
    a.pop()  # 从右边(尾部)移出元素
    print(a)  # (1,2,3) -> (2)
