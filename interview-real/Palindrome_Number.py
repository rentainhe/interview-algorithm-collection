class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # 小于0肯定不是回文串
            return False
        x=str(x)
        half_str = len(x)
        # 是不是回文串只需要考虑反转之后是否和原数组一样
        # 反转数组 x[::-1]
        return x[:half_str] == x[::-1][:half_str]