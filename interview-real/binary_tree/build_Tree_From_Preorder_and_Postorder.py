# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        # 或者是 if not post: return None
        # 先找到 root 节点
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        # 定位左子树和右子树的分界点
        # 注意这里的 + 1, 要对应 pre 里左子树的区间
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1: L + 1], post[:L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        return root


