# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        # 新建一个栈
        queue, res = [root], 0
        # 相当于二叉树的层序遍历, 二叉树的层数也就是depth, 可以使用相同的模板
        while queue:
            tmp = []
            for node in queue:  # 将这一层的所有节点添加进栈中
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res