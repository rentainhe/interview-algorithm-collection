# 二叉树的前序遍历和中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归解法，利用先序遍历找到根节点，之后在中序遍历中找到两个子树，再将利用先序遍历进行分割
        # 根节点就是preorder[0],在中序遍历序列中找到根节点的位置loc，以此划分左子树和右子树
        # 先序遍历中左子树为preorder[1:loc+1]；右子树为preorder[loc+1:]
        # 中序遍历中左子树为inorder[:loc]；右子树为inorder[loc+1:]
        # 递归结束的条件是，子树为空！即，inorder or preorder ==[]
        if preorder == []:
            return None
        loc = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:loc + 1], inorder[:loc])  # 注意这里的右边界要比实际下标+1
        root.right = self.buildTree(preorder[loc + 1:], inorder[loc + 1:])
        return root

        # 迭代解法：中心思想就是，先序遍历时两个连续的节点a,b；两者之间的关系只有两种可能：
        # 1.b是a的左孩子
        # 2.若a没有左孩子，b是a或者a祖先的右孩子(a可能是b的左兄弟树右下的节点，也就是说a是b的左兄弟树先序遍历完的最后一个节点)