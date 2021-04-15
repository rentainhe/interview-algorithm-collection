# encoding: utf-8

# binary search
# 二分查找
# 二分查找的前提是数组一定要有序

def binary_search(nums, target):
    # 找到开始和结束为止
    left = 0
    right = len(nums) - 1

    # 找到 target 的时候 left可能等于right
    while left <= right:
        mid = left + (right - left) // 2
        # mid = (left + right) // 2

        # 判断 target 是否等于中间的值
        if nums[mid] == target:
            return mid
        # 如果 target 比中间值小, 说明 [left : mid]这个区间里, 这里因为左闭右开其实相当于 left 到 mid-1
        if target < nums[mid]:
            right = mid - 1
        # 如果 target 比中间值大, 说明在 [mid+1: right]这个区间里
        elif target > nums[mid]:
            left = mid + 1
    return None


# 递归版本
def binary_search_v2(nums, target):
    n = len(nums)
    mid = n // 2
    if nums[mid] > target:
        binary_search_v2(nums[0:mid], target)
    elif nums[mid] < target:
        binary_search_v2(nums[mid + 1:], target)
    else:
        return mid


if __name__ == "__main__":
    nums = [5, 2, 3, 4, 6, 7, 8, 10]
    nums.sort()
    print("sorted nums: ", nums)
    print("target index: ", binary_search(nums, 3))  # 返回3的index
    print("target index: ", binary_search(nums, 1))  # 由于不存在1, 返回None
