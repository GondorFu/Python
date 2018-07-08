
# 可以使用r不对字符串进行转义
print('\\\t\\')
print(r'\\\t\\')

# 允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言
a = 123
print(a)
a = 'abc'
print(a)

# 除法
print(10/3)
print(10//3)

# 这里牵扯到文本文件的编码问题，对于英文，由于只有少量字符需要编码，
# 所以ASCII（一个字节）就能很好的表示所有的字母和控制符。
# 但对于中文，具体文字一个字节肯定放不下，所以就出现了很多不同的编码方式，
# 如Unicode所有字符采用2个字节编码，gbk使用了多字节来表示字符,
# 如果第一个字节是\x80以下，则仍然表示ASCII字符；而如果是\x80以上，
# 则跟下一个字节一起（共两个字节）表示一个字符。
# UTF-8使用变长编码，常用的英文字母被编码成1个字节，
# 汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

# 在计算机内存中，统一使用Unicode编码，
# 当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

# 所谓编码统一就是：文本所用的编码格式和让系统进行解码的格式必须一致。
# 其实就是在文本开头注明编写该文本所用的编码。

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')

# 注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，
# 但bytes的每个字符都只占用一个字节，且不能用encode编码。
# len函数计算的是str的字符数，如果换成bytes，len函数就计算字节数
print(len(b'abc'))
print(len('abc'))
print('abc'.encode('ascii'))
print(len('中文'))
utf_str = '中文'.encode('utf-8')
print(utf_str)
print(len(utf_str))

# 这个版本的python似乎默认UTF-8编码
# 因此如果文本编码使用UTF-8，就不需要特别声明解码格式。
# 但如果文本编码使用了其他格式，就需要在文本开头使用 
# coding = <coding name> , 比如 # coding = gbk
# # -*- coding: utf-8 -*-
# 的方式来进行注明。而且必须注意，编码方式的注明只能在文本开始的前两行使用。
import sys
print(sys.getdefaultencoding())

# 格式化输出
# %d	整数
# %f	浮点数
# %s	字符串，把任何数据类型转换为字符串
# %x	十六进制整数
print('growth rate: %d%%' % 7)
print('growth rate: %s%%' % 7)

s1 = 72
s2 = 85
print('''小明的成绩从去年的%d分提升到了今年的%d分，
小明的成绩提成了%2.1f%%'''
	% (s1, s2, (s2-s1)/s1*100))





