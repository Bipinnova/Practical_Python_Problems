# count how many times each number in list m appears in list n.

n = [2,3,4,7,5,3,4,6,2,3,3,5,5,1,9,11]
m = [10,11,6,3,4,5,2]


dic = {}

for i in n:
    dic[i] = dic.get(i,0)+1
    
result = []

for j in m:
    result.append(dic.get(j,0))
    
print(result)


# ✅ Time & Space Complexity:
# Time: O(n + m)
# 
# Space: O(u) where u is the number of unique elements in n