# Python的标准库提供了两个模块：_thread和threading，
# _thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0.1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 多线程和多进程最大的不同在于，多进程中，同一个变量，
# 各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
# 所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，
# 把内容给改乱了。
print('lock:')
import time, threading

balance = 0

def change_it(n):
	global balance
	balance += n
	balance -= n 
	
def run_thread(n):
	for i in range(100000):
		change_it(i)
		
t1 = threading.Thread(target = run_thread, args = (5, ))
t2 = threading.Thread(target = run_thread, args = (8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
# 究其原因，是因为修改balance需要多条语句，而执行这几条语句时，
# 线程可能中断，从而导致多个线程把同一个对象的内容改乱了。

balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target = run_thread, args = (5, ))
t2 = threading.Thread(target = run_thread, args = (8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# python有一个GIL锁：Global Interpreter Lock，
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，
# 也只能用到1个核。
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，
# 但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，
# 互不影响。

# 全局变量local_school就是一个ThreadLocal对象，
# 每个Thread对它都可以读写student属性，但互不影响。
# 你可以把local_school看成全局变量，
# 但每个属性如local_school.student都是线程的局部变量，
# 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()























