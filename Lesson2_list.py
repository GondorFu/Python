
# List
print()
print('List:——————————————————————————————————')
print(dir(list))

# 初始化
print()
print('初始化:————————————————————————————————')
a = list() # 表示一个空list
print(a)
a = list([None]) # list中有一个元素None
print(a)
print(len(a))
a = list([0 for x in range(5)])
print(a)
a = list([0, 1, 2, 3, 4, 5, [6.0, 6.1], [7]])
print(a)

# 引用元素
print()
print('引用元素:————————————————————————————————')
print(a[2])
print(a[-2])
print(a[6][1])
print(a[3:6]) # 必须按照[start:end:step]来引用, 且取start不取end
print(a[-1:3:-1]) 

# 添加元素
print()
print('添加元素:————————————————————————————————')
a.append(8)
print(a)
a.append([10])
print(a)
a.insert(-1, [9])
print(a)
a.extend([11, 12])  # 与append不同，extend将list中的每一个元素依此插入
print(a)
a += [13, 14]  # 功能与extend相同
print(a)

a.append(list())
print(a)
a.append([])
print(a)
print(a + list())  # 对a没有任何变化

# 删除元素
print()
print('删除元素:————————————————————————————————')
a.remove(1)  # 删除第一个相同的元素
print(a)
a_end = a.pop()
print('a:', a, 'a_end:', a_end)
a_2 = a.pop(2)
print('a:', a, 'a_2:', a_2)

a_copy = a.copy()
a_copy[2:5] = []
print(a_copy)
del a_copy[2:4]
print(a_copy)

# 直接赋值= a相当于给a起一个一个别名，操作对a仍然有效
a_clear = a.copy()  
a_clear.clear()
print('a_clear:', a_clear)


# 其他
print()
print('其他:————————————————————————————————')
print('长度：', len(a))

a.reverse()
print('翻转：', a)

def list2num(l):
    if isinstance(l, int): 
        return l 
    elif len(l) == 0: 
        return -1
    else:
        return l[0]
a.sort(key=list2num)
print('排序:', a)

a_reverse = sorted(a, key=list2num, reverse = True)
print('反向排序:', a_reverse)

a.append(4)
print(a)
print('4出现了%d次。' % a.count(4))
print('4第一次出现在了%s的位置上。' % a.index(4))

for v in a:  # 从list中依此选取，并不是一次性全部选取
    print(v)
    a.pop(1)

# 获得内部数据的下标
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

