# 替换空格

class Solution:
    def replaceSpace(self, s: str) -> str:
        split_string = s.split(" ")
        output_string = ""
        for i in range(len(split_string)-1):
            output_string += split_string[i] + "%20"
        output_string += split_string[-1]
        return output_string

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")
