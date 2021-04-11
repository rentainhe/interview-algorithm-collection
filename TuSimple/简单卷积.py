n, m = input().split(" ")
n = int(n)
m = int(m)
matrix = []
for i in range(n):
    matrix.append(input().split(" "))

kernel = []
for i in range(3):
    kernel.append(input().split(" "))

for i in range(0, n - 2):
    for j in range(0, m - 2):
        res = 0
        for k in range(3):
            for l in range(3):
                res += int(matrix[i + k][j + l]) * int(kernel[k][l])
        if j == m - 3:
            print(res)
        else:
            print(res, end=' ')  # 注意这里end的用法
