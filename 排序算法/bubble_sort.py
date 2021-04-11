a = [3, 4, 7, 1, 2, 8, 6, 3]


# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - i - 1):  # 注意区别下标和length，最大下标会比len多1
#             if arr[j + 1] < arr[j]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 假设有9个，则需要比较8轮，第一个比较8次，第二个比较7次
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n - i - 1):
            if arr[j+1]<arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    bubbleSort(a)
    print(a)
