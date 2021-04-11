n, m = input().split(" ")
matrix = []
for i in range(int(n)):
    matrix.append(input())
# 注意这里的都是str类型
cross = 0
for i in range(1, int(n) - 1):
    for j in range(1, int(m) - 1):
        if matrix[i][j] == "1":
            if matrix[i - 1][j] == "1" and matrix[i][j + 1] == "1" and matrix[i + 1][j] == "1" and matrix[i][
                j - 1] == "1":
                cross += 1

print(cross)
