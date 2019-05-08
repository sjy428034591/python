#!/usr/local/bin/python3
import getpass #导入模块
username = input("usename: ")
#getpass模块中，有一个方法也叫getpass
password = getpass.getpass("password: ")
if username == "bob" and password == "123456":
    print("login successful")
else:
    print("login incorrect")
