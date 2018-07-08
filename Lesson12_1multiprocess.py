
# 进程 Process 线程 Thread
# 线程是最小的执行单元，而进程由至少一个线程组成。

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，
# 使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

# import os
# print('Process (%s) start...' % os.getpid())
## Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
    # print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
    # print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

	
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
# 用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
	print('Parent process %s (%s)...' % (name, os.getpid()))
	
if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target = run_proc, args = ('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')

# 要启动大量的子进程，可以用进程池 Pool 的方式批量创建子进程：
# 对Pool对象调用join()方法会等待所有子进程执行完毕，
# 调用join()之前必须先调用close()，
# 调用close()之后就不能继续添加新的Process了。
# 请注意输出的结果，task 0，1，2，3是立刻执行的，
# 而task 4要等待前面某个task完成后才执行，
# 这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。

print('Pool')
print('Pool')
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end-start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
































































