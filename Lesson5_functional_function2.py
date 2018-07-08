# 函数作为返回值
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum

f = lazy_sum(1, 2, 3, 4)
print(f)
print(f())

# 闭包的执行逻辑
# 返回一个函数时，牢记该函数并未执行，
# 返回函数中不要引用任何可能会变化的变量。
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
print()

def count():
	def f(j):
		def g():
			return j*j
		return g 
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
# 匿名函数 lambda
# 匿名函数有个限制，就是只能有一个表达式，
# 不用写return，返回值就是该表达式的结果。
print(list(map(lambda x: x*x, [1, 2, 3])))

def build(x, y):
	return lambda : x*x + y*y
	
f = build(1, 2)
print(f())

# 装饰器
print('Decorator:———————————————————————————————————')
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
fb = build
print(fb.__name__)
print(f.__name__)
print()

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log  # 必须在作用函数定义之前标明
def now():
	print('Test Now')
now()
print()

import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('call %s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
	
@log('execute')
def now():
	print('Test Now')
now()
print()

# 编写一个decorator，
# 能在函数调用的前后打印出'begin call'和'end call'的日志
# 同时兼容是否输入字符串
def log(text):
	if isinstance(text, str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('call %s %s():' % (text, func.__name__))
				func(*args, **kw)
				print('end %s %s():' % (text, func.__name__))
				return
			return wrapper
		return decorator
	else:
		func = text
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('call %s():' % func.__name__)
			func(*args, **kw)
			print('end %s():' % func.__name__)
			return 
		return wrapper
	
@log
def now():
	print('now...')
	return
now()

@log('execute')
def now():
	print('now...')
	return
now()

# 偏函数 functools.partial 
print('Partial:————————————————————————————————————')
# 作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
import functools
int2 = functools.partial(int, base=2) 
print(int2('101001')) # kw = {'base':2} int('101001', **kw)
print(int2('101001', base = 10))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7)) # args = (10, 5, 6, 7) max(*args)













