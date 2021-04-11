n = input()
t, s, k = [], [], []

for i in range(int(n)):
    temp_list = input().split(" ")
    t.append(temp_list[0])
    s.append(temp_list[1])
    k.append(temp_list[2])

def rotate(string):
    last = string[-1]
    return last + string[:-1]


def compare(num1, num2, k):
    a = int(num1[-int(k):])
    b = int(num2[-int(k):])
    if a > b:
        return 1
    elif a < b:
        return 2
    else:
        return 3


for i in range(int(n)):
    a = t[i]
    b = s[i]
    len_a = len(a)
    len_b = len(b)
    _a = 0
    _b = 0
    string_a = ""
    string_b = ""
    while _a < int(k[i]):
        string_a += a
        a = rotate(a)
        _a += len_a
    while _b < int(k[i]):
        string_b += b
        b = rotate(b)
        _b += len_b
    if compare(string_a, string_b, k[i])==1:
        print("Tu")
    elif compare(string_a, string_b, k[i])==2:
        print("Simple")
    else:
        print("Draw")