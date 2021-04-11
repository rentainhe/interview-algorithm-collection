class Solution:
    def isStraight(self, nums: list[int]) -> bool:
        nums.sort()
        joker = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[-1] - nums[joker] < 5


class Solution2:
    def isStraight(self, nums: list[int]) -> bool:
        repeat = set()
        mi = 14
        ma = 0
        for num in nums:
            if num == 0: continue
            ma = max(ma, num)
            mi = min(mi, num)
            if num in repeat: return False
            repeat.add(num)
        return ma - mi < 5
