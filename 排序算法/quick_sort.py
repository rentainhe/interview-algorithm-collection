def quick_sort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more
# 利用了许多额外的空间

if __name__ == "__main__":
    a = [3, 4, 7, 1, 2, 8, 6, 3]
    print(quick_sort(a))

