
# 面向对象高级编程
# 给实例绑定一个方法
class Student():
	pass
s = Student()
def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 不能直接赋值，因为无法传递self变量
s.set_age(25)
print(s.age)  # 只对该实例有效

# 给类绑定方法
Student.set_age = set_age
s2 = Student()
s2.set_age(23)
print(s2.age)
# 通常情况下，上面的set_age方法可以直接定义在class中，
# 但动态绑定允许我们在程序运行的过程中动态给class加上功能，
# 这在静态语言中很难实现。

# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
	__slots__ = ('name', 'age')

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，
# 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

class GraduateStudent(Student):
	__slots__ = ()

# @propety
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值
# 只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		elif value < 0 or value > 100:
			raise ValueError('score must between 1-100')
		else:
			self._score = value
s = Student()
s.score = 60
print(s.score)

# 利用@property给一个Screen对象加上width和height属性，
# 以及一个只读属性resolution
class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, value):
		if not isinstance(value, (int, float)):
			raise ValueError('width must be a number!')
		elif value < 0:
			raise ValueError('width must be positive!')
		else:
			self._width = value
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, value):
		if not isinstance(value, (int, float)):
			raise ValueError('height must be a number!')
		elif value < 0:
			raise ValueError('height must be positive!')
		else:
			self._height = value
	@property
	def resolution(self):
		return self._width * self._height
		
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# 多重继承
# 一个子类就可以同时获得多个父类的所有功能
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。
class Animal(object):
	pass
class RunableMixIn(object):
	def run(self):
		print('Running...')
class Dog(Animal, RunableMixIn):
	pass
dog = Dog()
dog.run()

#定制类
# class中还有许多这样有特殊用途的函数，可以帮助我们定制类
# 直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，
# __repr__()是为调试服务的。

# 只有在没有找到属性的情况下，才调用__getattr__方法，动态返回一个属性
# __getattr__默认返回就是None。要让class只响应特定的几个属性，
# 我们就要按照约定，抛出AttributeError的错误
class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):  # 使用print的输出调用
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__  # 在命令行直接输入实例的输出调用
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student('Bob')
print(s)
s.score = 66
print(s.score)


# 如果一个类想被用于for ... in循环，类似list或tuple那样，
# 就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法，
# 拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
# 同理还有__setitem__()，__delitem__()

# 以斐波那契数列为例，写一个Fib类
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):  # 使类能够被循环调用
		return self
	def __next__(self):  # 迭代器取下一个数据
		self.a, self.b = self.b, self.a + self.b
		if self.a > 1000:
			raise StopIteration()
		return self.a
	def __getitem__(self, n):  # 像list一样选取数据
		if isinstance(n, int):
			a ,b = 1, 1
			for x in range(n):
				a, b = b, a+b
			return a
		elif isinstance(n, slice):
			start = n.start
			stop = n.stop
			step = n.step
			if start == None:
				start = 0
			if stop == None or stop < 0:
				raise ValueError('stop value is wrong!')
			if step == None:
				step = 1
			if step == 0:
				raise ValueError('step value is wrong!')
			a, b = 1, 1
			L = []
			flag = False
			if step < 0:
				step, start, stop, flag = -step, stop, start, True
			for x in range(stop):
				if x >= start and (x-start)%step == 0:
					L.append(a)
				a, b = b, a+b
			if flag:
				return list(reversed(L))
			return L

for n in Fib():
	print(n)

f = Fib()
print(f[3])
print(f[0:5])
print(f[0:11:2])
print(f[11:0:-2])

# 只有在没有找到属性的情况下，才调用__getattr__方法，动态返回一个属性
# __getattr__默认返回就是None。要让class只响应特定的几个属性，
# 我们就要按照约定，抛出AttributeError的错误
class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):  # 使用print的输出调用
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__  # 在命令行直接输入实例的输出调用
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student('Bob')
print(s)
s.score = 66
print(s.score)

# 使用__getattr__进行链式调用
class Chain(object):
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self, path):
		return Chain('%s\\%s' % (self._path, path))
	def __str__(self):
		return self._path
	__repr__ = __str__
	
print(Chain().status.user.timeline.list)

# 定义一个__call__()方法，就可以直接对实例像函数一样调用
# 通过callable()函数，判断一个对象是否是“可调用”对象
class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s' % self.name)
		
s = Student('Bob')
s()
print(callable(s))

# 枚举类
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
	'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# @unique装饰器可以帮助我们检查保证没有重复值。
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6	

day1 = Weekday.Mon
print(Weekday.Mon)
print(day1)
print(Weekday['Mon'])
print(Weekday.Mon.value)
print(Weekday(1))






































