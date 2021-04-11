# 反转元组、列表、字符串的方法

l = ['A', 'B', 'C']
x = reversed(l)
print(x)

x = tuple(reversed(l))
print(x)

# 反转字符串
s = 'ABC'
print(s[::-1])