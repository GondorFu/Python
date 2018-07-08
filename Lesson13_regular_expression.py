
# 正则表达式:用一种描述性的语言来给字符串定义一个规则
# \d 可以匹配一个数字，
# \w 可以匹配一个字母或数字，
# \s 可以匹配一个空格（也包括Tab等空白符）
# .  可以匹配任意字符
# *  表示任意个字符（包括0个），
# +  表示至少一个字符，
# ?  表示0个或1个字符，
# {n}表示n个字符，
# {n,m} 表示n-m个字符：
# [] 表示范围
# A|B 可以匹配A或B
# ^ 表示行的开头
# $ 表示行的结束

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

print('a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,\;]+', 'a b   c, d; e'))

# Group 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 正则表达式默认使用贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 如果一个正则表达式要重复使用几千次，出于效率的考虑，
# 我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，
# 直接匹配
import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

# 请尝试写一个验证Email地址的正则表达式。
# 版本一应该可以验证出类似的Email
# 版本二可以验证并提取出带名字的Email地址

import re

version_1 = re.compile(r'^[\w\d\.]+\@[\w\d]+\.com$')
print('版本一：','Found:', re.match(version_1,'someone@gmail.com').group())
print('        ','Found:',re.match(version_1,'bill.gates@microsoft.com').group())

version_2 = re.compile(r'^(<[\w\d\s]+>)?\s*([\w\d\.]+\@[\w\d]+\.[\w]+)$')
result = re.match(version_2,'<Tom Paris> tom@voyager.org').groups()
print('版本二：','Name:', result[0],'| Email:',result[1])














