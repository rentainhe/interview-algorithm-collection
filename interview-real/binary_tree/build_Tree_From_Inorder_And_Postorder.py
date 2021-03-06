# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder: return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        # 构建左子树
        root.left = self.buildTree(inorder[:index], postorder[:index])
        # 构建右子树
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

        return root
