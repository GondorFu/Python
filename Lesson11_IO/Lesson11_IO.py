
# IO编程
# 同步和异步的区别就在于是否等待IO执行的结果
# 如果是服务员跑过来找到你，这是回调模式，
# 如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。
# 总之，异步IO的复杂度远远高于同步IO。

# 如果文件不存在，open()函数就会抛出一个IOError的错误
try:
	f = open('test.txt', 'r')
	print(f.read())
finally:
	if f:
		f.close()

# 这和前面的try ... finally是一样的，但是代码更佳简洁，
# 并且不必调用f.close()方法。

with open('test.txt', 'r') as f:
	print(f.read())
	


# 反复调用read(size)方法，每次最多读取size个字节的内容
# 调用readlines()一次读取所有内容并按行返回list
f = open('test.txt', 'r')
print(f.read(8))
print(f.readline())

# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
f = open('thumb.jpg', 'rb')
print(f.read(8))
f.close()

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
# # 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
# 可选择直接忽略
f = open('test.txt', 'r', encoding = 'gbk', errors='ignore')
print(f.read())
f.close()

# 写文件调用open()函数时，传入标识符'w'或者'wb'
# 使用write将擦除原文件中的内容
# 表示写文本文件或写二进制文件：
f = open('test.txt', 'w')
f.write('Hello, world!')
f.close()

# 可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，
# 而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
# 所以，还是用with语句来得保险：

with open('test.txt', 'w') as f:
	f.write('Hello, world!')

# 从内存中读写数据
print()
print()
from io import StringIO
f = StringIO()
f.write('hello,')
f.write(' world!')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(len(s))
	print(len(s.strip()))
	print(s.strip())

# 如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 操作文件和目录
import os
# 操作系统的名字
print(os.name)
# 环境变量
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 然后创建一个目录:
os.mkdir(os.path.join(os.path.abspath('.'), 'testdir'))
# 删掉一个目录:
os.rmdir(os.path.join(os.path.abspath('.'), 'testdir'))
# 路径拆分，后一部分总是最后级别的目录或文件名
print(os.path.split(os.path.abspath('.')))
# 文件扩展名
print(os.path.splitext(os.path.abspath('.')))

# 新建文件
f = open('text1.txt', 'w')
f.close()
# 对文件重命名:
os.rename('text1.txt', 'test1.py')
# 删掉文件:
os.remove('test1.py')

# shutil模块提供了copyfile()的函数来复制文件

# 提取目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 提取.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and 
	os.path.splitext(x)[1] == '.py'])

# 编写一个程序，
# 能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
# 并打印出相对路径。

import os
def find_flie(p,ft):
    L=[x for x in os.listdir(p) if os.path.isfile(os.path.join(p,x)) and ft in x]
    L2=[os.path.join(p,x) for x in os.listdir(p) if os.path.isdir(os.path.join(p,x))]
    if L:
        for x in L:
            file_name=os.path.splitext(x)[0]
            file_types=os.path.splitext(x)[1]
            file_path=p
            print('%s %s %s'%(file_name,file_types,file_path))
    if L2:
        for x in L2:
            find_flie(x,ft)

def find_flie1():
    p = 'E:\WorkSpace\python' # input('你要寻找文件的目录是：')
    ft = 'py' # input('你要寻找文件名称包含：')
    a = '文件名'
    b = '文件类型'
    c = '文件路径'
    print('%5s%5s%5s'%(a,b,c))
    print('-----------------------------------------------------------------')
    find_flie(p,ft)

find_flie1()

# 序列化:把变量从内存中变成可存储或传输的过程
print()
print()
import pickle
d = dict(name = 'Bob', age = 20, score = 88)
d = {'name': 'Bob', 'age': 20, 'score': 88}
print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 反序列化
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

f = open('dump.txt', 'rb')
t = f.readline()
d = pickle.loads(t)
f.close()
print(d)


















