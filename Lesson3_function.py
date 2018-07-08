
# python内置函数
print(abs(-10))
print(max(10, 20))
print(int('123'))
print(float('12.34'))
print(str(123))
print(hex(255))

# 对计算机存储的理解，函数起别名，函数指针
a = abs
print(a(-10))

# 从其他文件中导入函数
from Lesson2_structure import my_abs
print(my_abs(-5))
# print(my_abs('A'))

# pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
	pass
	
# 通过tuple实现多值返回
import math
def move(x, y, step, angle=0):
	nx = x + step*math.cos(angle)
	ny = y - step*math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

r = move(100, 100, 60, math.pi/6)
print(r)

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解
def quadratic(a, b, c):
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) \
		or not isinstance(c, (int, float)):
		raise TypeError('bad operand type')
	elif b**2-4*a*c < 0:
		raise Exception('not exist solution')
	else:
		return (-b+math.sqrt(b*b-4*a*c))/2/a, (-b-math.sqrt(b*b-4*a*c))/2/a

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

# 默认参数:必选参数在前，默认参数在后，否则Python的解释器会报错
def power(x, n=2):
	s = 1
	while n>0:
		n -=1
		s = s*x;
	return s
print(power(2))
print(power(2, 3))

# 当不按顺序提供部分默认参数时，需要把参数名写上。
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Adam', 'M', city='Tianjin')

# 默认参数必须指向不变对象！
def add_end(L = []):
	L.append('END')
	print(L)

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，
# 不再是函数定义时的[]了。	
add_end()
add_end()

#可变参数
def calc(*number):
	sum = 0
	for n in number:
		sum += n*n;
	return sum

print(calc(1, 2))
print(calc(1, 2, 3))
print(calc(*[1,2,3,4]))
	

# 关键字参数
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
	
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 命名关键字参数
# 命名关键字参数必须传入参数名，这和位置参数不同。
# 如果没有传入参数名，调用将报错
def person(name, age, *, city, job):
	print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *args, city='Beijing', job):
	print(name, age, args, city, job)

person('Jack', 24, job='Engineer', city='Beijing')
person('Jack', 24, 'male', job='Engineer')

# 函数参数总结：
# 1、参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 2、关键字参数输入无顺序要求
# 3、默认参数输入无顺序要求
# 4、必须先输入必选参数，再输入默认参数
# 5、一旦选择city='Beijing'输入位置参数后，可变参数将失效
# 6、无命名的关键字参数将被放入kw中

def information(name, age, city='Beijing', job='engineer'
	, *args, gender='male', height, weight, **kw):
	print(name, age, city, job, args, gender, height, weight, kw)

information('Bob', 18, 'Tianjin', 'chief', 'YES',
	military='NO', weight=80, height=1.75, 
	color='yellow')

information('Bob', 18, job='chief', city='Beijing', 
	military='NO', weight=80, height=1.75, 
	color='yellow')

# 递归函数
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
	
# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

# 解决递归调用栈溢出的方法是通过尾递归优化。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
# 都只占用一个栈帧，不会出现栈溢出的情况。
# 不过，Python没有针对尾递归做优化
def fact(n):
	return fact_iter(n, 1)
	
def fact_iter(num, product):
	if num==1:
		return product
	return fact_iter(num-1, num*product)

print(fact(5))

# 汉诺塔的移动可以用递归函数非常简单地实现。
def move(n, a, b, c):
	if n==1:
		print(a, '-->', c)
	else:
		move(n-1, a, c, b)
		print(a, '-->', c)
		move(n-1, b, a, c)

move(3, 'A', 'B', 'C')














































