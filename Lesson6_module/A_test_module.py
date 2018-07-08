#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'GondorFu'

# 模块 module 包 package
# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
# 否则，Python就把这个目录当成普通目录，而不是一个包。

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 因为在加载模块时，会运行其中的程序。为了避免其中的可执行程序被执行，
# 通常使用如下判断来实现。只有直接运行该程序，__name__变量才等于__main__。
if __name__=='__main__':
    test()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

