string_list = input().split(" ")
y, k = int(string_list[0]), int(string_list[1])
hashmap = {}
hashmap[2014] = 0
hashmap[2015] = 1


def helper(y):
    if y in hashmap:
        return hashmap[y]
    else:
        result = helper(y - 2) ** 2 + k * helper(y - 1)
        hashmap[y] = result
        return result


mode = 10 ** 5 + 3

print(helper(y) % mode)
