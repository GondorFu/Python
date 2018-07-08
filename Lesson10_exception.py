# 打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1
# 可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
# 而是直接跳转至错误处理代码，即except语句块，执行完except后，
# 如果有finally语句块，则执行finally语句块，至此，执行完毕。

# Python内置的logging模块可以非常容易地记录错误信息：
# 常见异常：ZeroDivisionError ValueError(UnicodeError) TypeError AssertionError KeyError AttributeError IOError Exception BaseException
import logging
try:
	print('try...')
	r = 10/0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
	# raise
except ValueError as e:
	print('ValueError:', e)
except Exception as e:
	logging.exception(e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')

# 所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，
# 还把其子类也“一网打尽”。

# 抛出异常
print()
def bar():
	try:
		10/0
	except ZeroDivisionError:
		raise ValueError('input error!')
	print('END')
	
def main():
	try:
		bar()
	except ValueError as e:
		print('value error:', e)
	print('END')

main()

# 断言 assert 后续判断表达式应该为真
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
# 如果断言失败，assert语句本身就会抛出AssertionError：
n = 1
assert n!=0, 'n is zero!'

# 启动Python解释器时可以用-O参数来关闭assert
# E:\> python -O exception.py

# logging
# 这就是logging的好处，它允许你指定记录信息的级别，
# 有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，
# 最后统一控制输出哪个级别的信息。
print()
n = 1
import logging
logging.basicConfig(level = logging.INFO)
logging.info('n = %d' % n)
print('test')
print(10 / n)

# pdb 让程序以单步方式运行，可以随时查看运行状态。
# E:\> python -m pdb exception.py
# 输入命令l来查看代码
# 输入命令n可以单步执行代码
# 输入命令p 变量名来查看变量
# 输入命令q结束调试，退出程序

# 程序会自动在pdb.set_trace()暂停并进入pdb调试环境，
# 可以用命令p查看变量，或者用命令c继续运行
import pdb
pdb.set_trace()

# 目前比较好的Python IDE有PyCharm。
# 另外，Eclipse加上pydev插件也可以调试Python程序。

# 单元测试是用来对一个模块、一个函数或者一个类
# 进行正确性检验的测试工作。
# “测试驱动开发”（TDD：Test-Driven Development）
class Dict(dict):
	def __init__(self, **kw):
		super().__init__(**kw)
		
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribue '%s'" % key)
				
	def __setattr__(self, key, value):
		self[key] = value

# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，
# 测试的时候不会被执行

# 在单元测试中编写两个特殊的setUp()和tearDown()方法。
# 这两个方法会分别在每调用一个测试方法的前后分别被执行。
import unittest
class TestDict(unittest.TestCase):
	def setUp(self):
		print('setUp...')
	
	def tearDown(self):
		print('tearDown...')
	
	def test_init(self):
		d = Dict(a=1, b='test')
		# 断言函数返回的结果与1相等
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))
	
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')
		
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')
		
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError): 
		# 通过d['empty']访问不存在的key时，断言会抛出KeyError
			value = d['empty']
	
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

# 推荐：E:\>python -m unittest mydict_test			
if __name__ == '__main__':
	unittest.main()

# 文档测试
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()









































