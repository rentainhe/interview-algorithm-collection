# 假设前面是从小到大排序好的部分
def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):  # 不断和前面的比较，找到适合的插入位置即可，因为前面的已经是排序好的了
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


if __name__ == "__main__":
    a = [3, 4, 7, 1, 2, 8, 6, 3]
    insert_sort(a)
    print(a)
