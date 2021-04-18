from typing import List

# 二叉搜索树: 左子树上所有节点的值不大于其根节点
# 右子树上所有节点的值不小于其根节点
# 任意节点的左右子树也分别为二叉搜索树

# 二叉搜索树的后序遍历
# 后序遍历: 左 - 右 - 中
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 二叉搜索树的性质：
        # 如果左子树不空，左子树的所有节点的值小于根节点的值。
        # 如果右子树不空，则右子树所有节点的值大于根节点的值。
        # 当 postorder 为空的时候返回 True
        if postorder == []: return True
        n = len(postorder)
        # 找到第一个大于根节点的数，如果这个是二叉搜索树的话，这个数之后的数都是属于右子树，这个数之前的数都是属于左子树
        for i in range(n):
            if postorder[i] > postorder[-1]:
                break
        # postorder[-1] 是当前后序遍历的根节点
        # 并且按照上面的遍历方法来看，这里的left_tree里不会出现大于根节点的数
        left_tree = postorder[:i]
        right_tree = postorder[i:n - 1]
        # 判断right_tree里是否有小于根节点的数，有的话返回False
        for num in right_tree:
            if num < postorder[-1]:
                return False
        return self.verifyPostorder(left_tree) and self.verifyPostorder(right_tree)

