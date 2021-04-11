a = [3, 4, 7, 1, 2, 8, 6, 3]


def selectSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i  # 需要替换的index
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:  # 这样写好像交换次数更多
                arr[min_idx], arr[j] = arr[j], arr[min_idx]


def selectSortV2(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i  # 初始化一个起始的index
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j  # 找到最小值的下标
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    selectSortV2(a)
    print(a)
