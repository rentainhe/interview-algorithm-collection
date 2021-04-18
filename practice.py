nums = [3,1,1,1,2,2]
hashmap = {}
for i in nums:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i] += 1
hashmap = sorted(hashmap.items(), key=lambda x:x[1], reverse=False)

print(hashmap)
