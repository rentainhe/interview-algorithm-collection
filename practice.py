from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(*matrix)
print(list(zip(*matrix)))