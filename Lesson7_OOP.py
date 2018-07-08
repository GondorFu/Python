
# 面向对象编程 Objects Orients Programming
# 类 class；实例 instance
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def print_score(self):
		print('%s:%s' % (self.name, self.score))
		
lisa = Student('Lisa Simpson', 87)
lisa.print_score()
lisa.age = 18
print(lisa.score)

# 数据封装
# 实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，
# 可以直接在类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	
	def print_score(self):
		print('%s:%s' % (self.__name, self.__score))
lisa.print_score()
# print(lisa.__score) # 其实Python只是将__score用_Student__score进行了替换

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
# 并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
# 不是private变量，所以，不能用__name__、__score__这样的变量名。
# 看到以一个下划线开头的实例变量名，比如_name，
# 这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
# 当你看到这样的变量时，意思就是，“虽然我可以被访问，
# 但是，请把我视为私有变量，不要随意访问”。

lisa.__score = 59
print(lisa.__score)
lisa.print_score() # 只是给另一个__score赋了一个值，原值没变

# 继承 子类Subclass；基类Base class; 父类或超类Super class
# 多态：子类的函数覆盖了父类的函数
class Animal(object):
	def run(self):
		print('Animal is running')
	def run_twice(self):
		self.run();
		self.run();
		
class Dog(Animal):
	def run(self):
		print('Dog is running')
		
dog = Dog()
dog.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

dog.run_twice()

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Dog())
# 这就是著名的“开闭”原则：对扩展开放，对修改封闭

class Timer(object):
	def run(self):
		print('Starting...')
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
# 一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# 感觉就是变量不再需要类型声明造成的
run_twice(Timer())

# types
import types
def fn():
	pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# dir
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list
print(dir('ABC'))

# 在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
	def __init__(self):
		self.weight = 18
	def __len__(self):
		return 100
	def get_weight(self):
		print(self.weight)

dog = MyDog()
print(len(dog))

print(hasattr(dog, 'weight'))
print(hasattr(dog, '__len__'))
print(hasattr(dog, 'get_weight'))
print(setattr(dog, 'weight', 20))
print(getattr(dog, 'weight', 'not exist'))
print(getattr(dog, 'height', 'not exist'))

d = {'a':1, 'b':2, 1:3}
print(d.get('a', -1))
print(getattr(d, '1', -1))

print()
print()

# 实例属性和类属性
class Cat(Animal):
	name = 'Cat'
# 千万不要把实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
cat = Cat();
print(cat.name)
cat.name = 'Bosi'
print(cat.name)
print(Cat.name)
del cat.name
print(cat.name)











