from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [0 for _ in range(len(arr))]  # 用来记录某节点是否访问过
        length = len(arr)

        def dfs(pos):
            if visited[pos] == 1:  # 代表之前访问过的点又被访问了一次，说明出现了循环，则不可能满足题意
                return False
            if arr[pos] == 0 and visited[pos] == 0:  # 某个点没访问过，且其值为0
                return True
            visited[pos] = 1  # 如果都不是上面的情况，就设当前点已经访问
            left, right = False, False  # 向左或者向右跳能否成功的标记
            # 跳跃后的范围在数组下标范围内才可以进行dfs
            if 0 <= pos - arr[pos] < length:
                left = dfs(pos - arr[pos])
            if 0 <= pos + arr[pos] < length:
                right = dfs(pos + arr[pos])
            return right or left  # 只要左右有一边有合理的路径即可

        return dfs(start)