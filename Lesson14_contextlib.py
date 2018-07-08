# contextlib
# Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭
# 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


# 这样我们就可以把自己写的资源对象用于with语句：
with Query('Bob') as q:
    q.query()
	
print()
# 编写__enter__和__exit__仍然很繁琐，
# 因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

# @contextmanager这个decorator接受一个generator，
# 用yield语句把with ... as var把变量输出出去，
# 然后，with语句就可以正常地工作了：
with create_query('Bob') as q:
    q.query()

# 很多时候，希望在某段代码执行前后自动执行特定代码，
# 也可以用@contextmanager实现。例如：
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

# 如果一个对象没有实现上下文，我们就不能把它用于with语句。
# 这个时候，可以用closing()来把该对象变为上下文对象。
# 例如，用with语句使用urlopen()：

from contextlib import closing
from urllib.request import urlopen

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
# 它的作用就是把任意对象变为上下文对象，并支持with语句。

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)



























