
# 定义函数，并通过isinstance来对输入数据类型进行判断
def my_abs(a):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	if a>=0:
		return a
	else:
		return -a

# List
print('List:————————————————————————————————')
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[2])
print(classmates[-2])

classmates.append(['Adam',])
classmates.append(list())
classmates.insert(1, 'Jack')
print(classmates)
print(len(classmates))


classmates.reverse()
print(classmates + list())
classmates += [None,]
print(classmates)


nameLast = classmates.pop()
print(nameLast)
print(classmates)
name1 = classmates.pop(1)
print(name1)
print(classmates)

L = ['Apple', 123, True]

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s[2][1])
print(len(s))

# 获得内部数据的下标
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

# Tuple，一旦初始化后不能修改
print('Tuple:————————————————————————————————')
classmates = ('Michael', 'Bob', 'Tracy')
# 在定义一个数时，会与数学公式中的小括号相冲突。
# 所以python在这种情况下，默认这是一个数。想要定义一个tuple
t = (1)
print(t)
print(type(t))
t = (1,)
print(t)
print(type(t))

# 计算机的存储机制
a = 'abca'
print('a=%s' % a)
print('a.replace=%s' % a.replace('a', 'A')) # 创建了一个新的空间，进行改变
print('a=%s' % a)

# 但了解计算机存储会知道，其实tuple只是限制了指向不变。
# 通过在其中添加List，就能方便地定义一个可以修改的tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
height = 1.75 # int(input('请输入您的升高：'))
weight = 80.5 # int(input('请输入您的体重：'))
BMI = weight/height**2
print('您的BMI指数为：%2.2f, ' % BMI, end='') # 不换行

# import sys
# sys.stdout.write('您的BMI指数为：%2.2f, ' % BMI)

if BMI < 18.5:
	print('过轻')
elif BMI < 25:
	print('正常')
elif BMI < 28:
	print('过重')
elif BMI < 32:
	print('肥胖')
else:
	print('严重肥胖')

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello, %s' % name)

# dictionary dict
print('Dict:————————————————————————————————')
# 检索迅速但需要由于使用Hash,占用较大空间
# 同时由于key不可变，所以List不能作为Key
d = {'Michael' : 95, 'Bob': 75, 'Tracy': '85', 2: 'Joe'}
print(d['Bob'])
print(d[2])
print('Thomas' in d)

# 返回value,如果不存在返回后面的输入值
print(d.get('Bob', -1))
print(d.get('Thomas', -1))

print(d.pop('Bob'))
print(d)

# set 集合
print('Set:————————————————————————————————')
# set和dict的唯一区别仅在于没有存储对应的value.
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象
s = set([1,2,3,1])
print(s)
s.add(4)
s.remove(2)

# 集合的交与并
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)













