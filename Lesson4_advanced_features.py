
# Slice 切片 [0, 1, 2, ... , -3, -2, -1]
# [start, stop, step]
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[1:3])
print(L[:3])
print(L[-1:-3])
print(L[-2:])
print(L[-1:-3:-1])
print('abcdef'[2:5])

# Iteration 迭代
# dict的迭代
d = {'a':1, 'b':2, 'c':3}
for key in d:
	print(key)
print()

for key in d.keys():
	print(key)
print()

for value in d.values():
	print(value)
print()

for key, value in d.items():
	print(key, value)
print()

# 可以通过Iterable来判断是否可以迭代
from collections import Iterable
print(isinstance('abc', Iterable))

# 获得内部数据的下标
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

# List Comprehensions 列表生成式
print(list(range(1,11)))
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'abc' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

d = {'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])

L1 = ['Hello', 'World', 18, 'Apple', None]
# isinstance() lower() upper() capitalize()
print([v.lower() for v in L1 if isinstance(v, str)])
print([v.upper() for v in L1 if isinstance(v, str)])
print([v.capitalize() for v in L1 if isinstance(v, str)])

# generator 生成器:一边循环一边计算的机制，不直接产生所有数据占用内存
g = (x*x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
# 用完之后就没了
g = (x*x for x in range(10))
for n in g:
	print(n)

# 斐波拉契数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a+b
		n += 1
	return 'done'

print(fib(6))

# generator 斐波拉契数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print('test before')
		yield b
		print('test after')
		a, b = b, a+b 
		n += 1
	return 'done'

# 发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，
# 返回值包含在StopIteration的value中
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
	
# 杨辉三角
def triangles():
	L = [1]
	yield L
	L = [1, 1]
	yield L
	n = 3
	while True:
		for i in range(n-1, 0, -1):
			if i == n-1:
				L.append(1)
			elif i != 0:
				L[i] = L[i] + L[i-1]
		yield L
		n += 1

n = 0
for t in triangles():
	print(t)
	n += 1
	if n == 10:
		break
print()

# 迭代器 Iterator
# Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，
# 例如全体自然数。而使用list是永远不可能存储全体自然数的。
# Python的for循环本质上就是通过iter()，并不断调用next()函数实现的
from collections import Iterable, Iterator
print(isinstance(triangles(), Iterable))
print(isinstance(triangles(), Iterator))
print(isinstance(triangles(), Iterator))
print()
print(isinstance('abc', Iterable))
print(isinstance('abc', Iterator))
print(isinstance(iter('abc'), Iterator))
print()











