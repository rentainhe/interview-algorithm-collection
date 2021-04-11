# encoding: utf-8

# 暴力解法
def count(x, y):
    smaller = x if x < y else y
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            max_hcf = i
        else:
            pass

    larger = x if x > y else y
    while True:
        if larger % x == 0 and larger % y == 0:
            min_lcm = larger
            break
        else:
            larger += 1
    return [max_hcf, min_lcm]


print(count(7, 45))
