# 输入一个二维数组和一个数字，要求完成快速查找, 二维数组内的每一个列表都是递增
# 每一行都是从左向右递增，每一列都是从上向下递增
# 例如[[1,3,5,6,8], [2,4,5,7,9]]

# 初始化一个指向右上角矩阵右上角的元素，因为这个元素具有的特性是，比他小的值，都在其左侧，比它大的值都在下方
def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
    i, j = len(matrix) -1 , 0
    while i>=0 and j<len(matrix[0]):
        if matrix[i][j] > target: i-=1
        elif matrix[i][j] < target: j += 1
        else: return True
    return False


