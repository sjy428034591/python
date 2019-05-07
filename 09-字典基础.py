#!/usr/local/bin/python3
#字典是key-value（键一值）对形式的，没有顺序，通过键取出值
adict = {"name": "bob", "age": 23}
print(adict)
len(adict)
print("bob" in adict)
print("name" in adict)
adict["email"] = "bob@tedu.com" #字典中没有key，则添加新项目
print(adict)
adict["age"] = 25 #字典中已有key，修改对应得value 
print(adict)
