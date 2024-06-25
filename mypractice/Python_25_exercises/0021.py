'''
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

    阅读资料 用户密码的存储与 Python 示例 http://zhuoqiang.me/password-storage-and-python-example.html

    阅读资料 Hashing Strings with Python http://www.pythoncentral.io/hashing-strings-with-python/

    阅读资料 Python's safest method to store and retrieve passwords from a database http://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database
'''
import os
import hashlib


def encrypt_password(password):
    salt = os.urandom(8)
    result = hashlib.sha256(password.encode()+salt).hexdigest()
    return salt, result


def check_password(user, password):
    salt = user['salt']
    return hashlib.sha256(password.encode()+salt).hexdigest() == user['password']

user = {'password': '', 'salt': b''}
raw_password = 'password'
user['salt'], user['password'] = encrypt_password(raw_password)
result = check_password(user, raw_password)
print(result)

'''
__author__ = 'Drake-Z'

import hashlib
from collections import defaultdict
db = {}
db = defaultdict(lambda: 'N/A')                     #去掉登录可能产生的KeyError

def get_md5(password):
    a = hashlib.md5()
    a.update(password . encode('utf-8'))
    return (a.hexdigest())

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    b = get_md5(password + username + 'the-Salt' )
    if b==db[username]:
        return True
    else:
        return False
a = input('注册输入用户名：')
b = input('注册输入密码：')
register(a, b)
a = input('登录输入用户名：')
b = input('登录输入密码：')
print(login(a, b))
'''