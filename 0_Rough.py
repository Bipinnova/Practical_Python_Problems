s = 'azyxyyzazaaaa'
q = ['d', 'a', 'y', 'z']

dic_char = {}

for i in s:
    dic_char[i] = dic_char.get(i,0) + 1
    
result = []

for j in q:
    result.append(dic_char.get(j, 0))

print(result)