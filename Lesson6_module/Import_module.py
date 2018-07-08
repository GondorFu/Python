
# 导入其他.py文件中的函数
# 导入时会将导入文件运行一遍
# 在同一路径下
import Imported_module
Imported_module.test1()

from Imported_module import test2
test2()
Imported_module.test2()

# 不在同一路径下
# 模块搜索路径
import sys
print(sys.path)

# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录：
# 这种方法是在运行时修改，运行结束后失效。
# 第二种方法是设置环境变量PYTHONPATH，
# 该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。
# 注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
sys.path.append('E:\WorkSpace\python')

import Lesson0_introduction
Lesson0_introduction.test()

from Lesson0_introduction import test
test()

























