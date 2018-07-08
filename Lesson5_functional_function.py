
# 函数式编程 Functional Programming:高度抽象的编程范式
# 高阶函数 Higher-order function:将函数作为参数输入
def add(x, y, abs):
	print(abs(x) + abs(y))

add(-5, 6, abs)

# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
	return x*x

print(list(map(f, [1, 2, 3, 4, 5])))

print(list(map(str, [1, 2, 3, 4])))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x, y):
	return x+y

print(reduce(add, [1, 2, 3, 4]))
print(sum([1, 2, 3, 4]))

# str转int
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
		'6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
	return reduce(lambda x, y: x*10+y, map(char2num, s))

print(str2int('12345'))

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
	return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 求素数
def natureNum():
	n = 2
	yield n
	while True:
		n += 1
		yield n

# 当函数需要两个输入参数，又想用map, reduce, filter时可以使用
# 将一个函数中输入其他参数，再通过lambda返回需要参数函数的形式。
def deleteNum(n):
	return lambda x: x%n > 0

def primes():
	it = natureNum();
	while True:
		n = next(it)
		yield n
		it = filter(deleteNum(n), it)

for n in primes():
	if n < 100:
		print(n)
	else:
		break

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
def is_palindrome(n):
	return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1,1000));
print(list(output))

# sorted 排序
l = [36, 5, -12, 9, -21]
print(sorted(l))
print(l)
print(l.sort())
print(l)

# 将key函数作用于每一个元素，并对返回值进行排序。
# 最后按照顺序将原数据输出
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 用sorted()对上述列表分别按名字排序
def by_name(t):
	return t[0].lower()
	
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
	return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)	


























