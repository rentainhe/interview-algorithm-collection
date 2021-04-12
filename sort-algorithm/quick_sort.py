# version 2
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

# version 2
def quick_sort2(nums, i, j):
    if i >=j:
        return nums
    pivot = nums[i]
    low = i
    high = j
    while i<j:
        while i<j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i<j and nums[i] <= pivot:
            i += 1
        nums[i] = nums[j]


if __name__ == "__main__":
    a = [3, 4, 7, 1, 2, 8, 6, 3]
    print(quick_sort(a))

