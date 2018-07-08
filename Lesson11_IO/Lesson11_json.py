
# 序列化：把变量从内存中变成可存储或传输的过程
# 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening

# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
# 比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
# 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON (JavaScript Object Notation) 不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
print('JSON:')
import json
d = dict(name = 'Bob', age = 20, score = 88)
print(json.dumps(d))
f = open('dump.txt', 'w')
f.write(json.dumps(d))
f.close()

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

# 类的实例序列化
class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
		
def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

s = Student('Bob', 20, 88)
print(json.dumps(s, default = student2dict))
print(json.dumps(s, default = lambda obj: obj.__dict__))

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])
	
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook = dict2student))
















