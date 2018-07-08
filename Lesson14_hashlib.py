# hashlib
# Python的hashlib提供了常见的摘要算法(又称哈希算法、散列算法)，如MD5，SHA1等等。
# 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
# （通常用16进制的字符串表示）。

# 以常见的摘要算法MD5为例
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 另一种常见的摘要算法是SHA1
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# 这一个简单的应用是数据库中的用户名和密码的存储
# 要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），
# 只能用于防篡改，但是它的单向计算特性决定了
# 可以在不存储明文口令的情况下验证用户口令。
print()
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
import hashlib
db={}

def get_md5(word):
    md5=hashlib.md5()
    md5.update(word.encode('utf-8'))
    return ( md5.hexdigest())

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    p=get_md5(password+username+'the-Salt')
    if username in db :
        if  db[username]==p:
            print('Login Successful')
            return 1
        else:
            print('Password is wrong')
            return 0
    else:
        print('Can not find',username)
        return -1

while True:
    x=input('register:1 login:2 quit:0\n')
    if x == '0':
        break
    elif x == '1':
        username=input('Input your username:\n')
        password=input('Input your password:\n')
        register(username,password)
    elif x=='2':
        username=input('Input your username:\n')
        password=input('Input your password:\n')
        login(username,password)
    else:
        print('wrong')

























