# interview-algorithm-collection
A collection of interview algorithm problems and solutions

## Good notes online
- [__python实现二叉树的遍历以及基本操作__](https://www.cnblogs.com/anzhengyu/p/11083568.html)
- [__【LeetCode】代码模板, 刷题必会__](https://blog.csdn.net/fuxuemingzhu/article/details/101900729)
- [__回溯算法套路详解__](https://zhuanlan.zhihu.com/p/93530380)

## Good learning website
- [__labuladong的算法小抄__](https://labuladong.gitbook.io/algo/)

## Basic knowledge
|code|algorithm|method|
|:---:|:---:|:---:|
|[__binary search__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/search-algorithm/binary_search.py)|__查找算法__|__二分查找__|
|[__sort algorithm__](https://github.com/rentainhe/interview-algorithm-collection/tree/master/sort-algorithm)|__经典排序算法__|__快速排序, 冒泡排序, 插入排序, 选择排序__|


## Content
|question|leetcode-number|answer|method|
|:---:|:---:|:---:|:---:|
| __计算IOU__ | ... | [__IoU.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/IoU.py)|...|
| __求两个数的最小公倍数和最大公约数__ | ... | [__最小公约和最大公倍__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/%E6%9C%80%E5%B0%8F%E5%85%AC%E7%BA%A6%E5%92%8C%E6%9C%80%E5%A4%A7%E5%85%AC%E5%80%8D.py)|...|
| __最小路径和__ | [__leetcode-64__](https://leetcode-cn.com/problems/minimum-path-sum/) | [__minimum_path_sum.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/minimum_path_sum.py)| __动态规划__ |
| __盛水最多的容器__ | [__leetcode-11__](https://leetcode-cn.com/problems/container-with-most-water/) | [__most_water.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/most_water.py)| __双指针-左右指针__ |
| __删除链表的倒数第N个结点__ | [__leetcode-19__](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) | [__remove_node.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/remove_node.py)| __双指针-快慢指针-使用dummy head小技巧__ |
| __最长回文子串__ | [__leetcode-5__](https://leetcode-cn.com/problems/longest-palindromic-substring/)| [__longest_palindromic_substring.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/longest_palindromic_substring.py)| __动态规划或者中心扩散__ |
| __最接近的三数之和__ | [__leetcode-16__](https://leetcode-cn.com/problems/3sum-closest/)|[__3sum_closest.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/3sum_closest.py) <br> [__leetcode-优质题解__](https://leetcode-cn.com/problems/path-sum-ii/solution/tao-mo-ban-er-cha-shu-wen-ti-de-dfs-he-bfs-jie-fa-/)| __数组排序-双指针__ |
| __路径总和II__ | [__leetcode-113__](https://leetcode-cn.com/problems/path-sum-ii/)|[__path_sum_ii.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/path_sum_ii.py)| __BFS算法, DFS算法, 注意题目要求__ |
| __从上到下打印二叉树__ | [__剑指 Offer 32__](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)| [__print_tree.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/print_tree.py) | __BFS算法__ |
| __全排列__ | [__leetcode-46__](https://leetcode-cn.com/problems/permutations/) | [__Permutations.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/backtrack/permutations.py) | __回溯法__ |
| __全排列II__ | [__leetcode-47__](https://leetcode-cn.com/problems/permutations-ii/) | [__Permutations_II.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/backtrack/Permutations_II.py) | __回溯法__ |
| __组合总和__ | [__leetcode-39__](https://leetcode-cn.com/problems/combination-sum/) | [__Combination_Sum.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/backtrack/Combination_Sum.py) | __回溯法__ |
| __组合总和II__ | [__leetcode-40__](https://leetcode-cn.com/problems/combination-sum-ii/) | [__Combination_Sum_II__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/backtrack/Combination_Sum_II.py) | __回溯法__ |
| __矩阵中的路径__ | [__剑指 Offer 12__](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/) | [__Exist_path_in_matrix.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/backtrack/Exist_path_in_matrix.py) | __DFS回溯, 注意剪枝条件__ |
| __从前序与中序遍历序列构造二叉树__ | [__leetcode-105__](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) <br> [__剑指 Offer 07__](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/) | [__build_Tree_From_Preorder_And_Inorder.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/binary_tree/build_Tree_From_Preorder_And_Inorder.py) | __迭代递归__ |
| __从中序和后序遍历序列构造二叉树__ | [__leetcode-106__](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [__build_Tree_From_Inorder_And_Postorder.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/binary_tree/build_Tree_From_Inorder_And_Postorder.py) | __迭代递归__ |
| __从前序和后序遍历序列构造二叉树__ | [__leetcode-889__](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | [__build_Tree_From_Preorder_And_Postorder.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/binary_tree/build_Tree_From_Preorder_And_Postorder.py) | __迭代递归__ |
| __二叉搜索树的后序遍历序列__ | [__剑指 Offer 33__](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/) | [__offer-33.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/%E5%89%91%E6%8C%87offer/offer-33.py) | __递归__ |
| __二叉树的深度__ | [__剑指 Offer 55__](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/) | [__Depth_of_Binary_Tree.py__]() | __用栈实现, 方法类似于层序遍历__ |
| __连续子数组的最大和__ | [__剑指 Offer 42__](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/) | [__Maximum_Subarray.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/Maximum_Subarray.py) | __动态规划__ |
| __礼物的最大价值__ | [__剑指 Offer 47__](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/) | [__offer-47.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/%E5%89%91%E6%8C%87offer/offer-47.py) | __动态规划__ |
| __最长不含重复字符的子字符串__ | [__剑指 Offer 48__](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/) | [__offer-48.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/%E5%89%91%E6%8C%87offer/offer-48.py) | __快慢指针__ |
| __字符串的排列__ | [__剑指 Offer 38__](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/) | [__offer-38.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/%E5%89%91%E6%8C%87offer/offer-38.py) | __回溯 + 剪枝__ |
| __数组中出现次数超过一半的数字__| [__剑指 Offer 39__](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/) | [__offer-39.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/%E5%89%91%E6%8C%87offer/offer-39.py) | __哈希表__ |
| __前k个高频元素__ | [__leetcode-347__](https://leetcode-cn.com/problems/top-k-frequent-elements/) | [__Top_K_Frequent_elements.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/Top_K_Frequent_elements.py) | __构建hashmap, 字典排序__ |
| __合并区间__ | [__leetcode-56__](https://leetcode-cn.com/problems/merge-intervals/) | [__Merge_Intervals.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/Merge_Intervals.py) | __对数组进行排序, 然后按顺序添加__ |
| __不同路径__ | [__leetcode-62__](https://leetcode-cn.com/problems/unique-paths/) | [__Unique_Paths__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/dp/Unique_Paths.py) | __动态规划__ |
| __不同路径 II__ | [__leetcode-63__](https://leetcode-cn.com/problems/unique-paths-ii/) | [__Unique_Paths_II__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/dp/Unique_Paths_II.py) | __动态规划, 注意和上题初始化的不同__ |
| __最长回文子串__ | [__leetcode-5__](https://leetcode-cn.com/problems/longest-palindromic-substring/) | [__longest_palindromic_substring.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/dp/longest_palindromic_substring.py) | __动态规划__ |
| __最长递增子序列__ | [__leetcode-300__](https://leetcode-cn.com/problems/longest-increasing-subsequence/) | [__Longest_Increasing_Subsequence.py__](https://github.com/rentainhe/interview-algorithm-collection/blob/master/interview-real/dp/Longest_Increasing_Subsequence.py) | __动态规划__ |






