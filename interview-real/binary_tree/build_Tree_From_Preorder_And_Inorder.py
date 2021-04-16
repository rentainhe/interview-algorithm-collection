# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])

        # 因为没有重复元素, 所以可以直接根据值来查找根节点在中序遍历中的位置
        # 中序遍历中, 对应root元素左边的是左子树, 右边的是右子树
        mid = inorder.index(preorder[0])

        # 无论是在 preorder 还是 inorder
        # preorder[:mid+1] 都是root左边
        # preorder[mid+1:] 都是root右边
        # inorder[:mid] 都是root左边
        # inorder[mid+1:] 都是root右边

        # 构建左子树
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # 构建右子树
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
