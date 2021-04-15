# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []  # 特殊情况处理
        queue = [root]
        res = []
        while queue:
            for node in queue:
                res.append(node.val)
            ll = []
            for node in queue:
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            queue = ll
        return res


from collections import deque

# 通用格式
class SolutionV2:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
