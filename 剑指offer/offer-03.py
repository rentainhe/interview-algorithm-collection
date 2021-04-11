# 只需要找到list中的某个重复元素，所以一种方法是只需要对这个list进行分类，然后查看相邻元素中是否有相同的，有的话直接return
# 时间上O(nlogn)， 空间上O(1)
def findRepeatNumber(nums):
    nums.sort()
    pre = nums[0]
    for i in range(1, len(nums)):
        if pre == nums[i]:
            return pre
        else:
            pre = nums[i]

# use hash map
# 构建一个字典，如果字典中包含这个key，那么
def findRepeatNumber_hash(nums):
    repeatDict = {}
    for num in nums:
        if num not in repeatDict:
            repeatDict[num] = 1
        else:
            return num

# 鹊巢原理
# 因为题目中给的元素是 < len(nums)的，所以我们可以让位置i的地方放元素i，如果位置i的元素不是i的话，那么我们就把i元素的位置放到它应该放的位置，即
# nums[i] 和 nums[nums[i]]交换，这样就把原来在nums[i]的位置元素正确归位了，如果在归为的时候发现了那个位置上的元素和要归位的元素一致，说明重复
def findRepeatNumber_V2(nums):
    n = len(nums)
    for i in range(n):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            temp = nums[i]
            nums[i], nums[temp] = nums[temp], nums[i]

if __name__ == "__main__":
    test = [1, 2, 3, 3, 4, 5, 5]
    print(findRepeatNumber(test))
    print(findRepeatNumber_hash(test))
    print(findRepeatNumber_V2(test))