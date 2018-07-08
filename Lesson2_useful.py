# range函数使用
m = 1
n = 10
# 0 - n-1
print([i for i in range(n)])
# m - n-1
print([i for i in range(m, n)])
# n - m+1
print([i for i in range(n, m, -1)])

# 字符串处理
li = ['my','name','is','bob']
li_join = '_'.join(li)
print(li_join)
li_split = li_join.split('_')
print(li_split, li_split == li)
li_split_2 = li_join.split('_', 2) # 只分离两个
print(li_split_2)

s = 'abc'
s_join = ' '.join(s)
print(s_join)
s_split = s_join.split(' ')
print(s_split, s_split == s, ''.join(s_split) == s)

l = [[1, 3, 5, 7],[2, 4, 7, 8],[3, 5, 9, 10]]
print(list(map(lambda x: x[0:2], l[1:3])))

# dict遍历
d = {0:0, 1:1, 2:2}
for key in d:
    print(key)
    
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

























