
# 集合 collections
# namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p, tuple))
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque([None, 'a', 'b', 'c'])
print(q[0])
q.append('x')
print(q.pop())
q.appendleft('y')
print(q.popleft())
print(q)

# defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
print(dd['key1'])

# OrderedDict
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# 实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self.capacity = capacity
	
	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self_capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)

# Counter 实际上也是dict的一个子类
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
	
print(c)

























