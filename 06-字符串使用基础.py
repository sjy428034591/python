sentence = "tom\"s pet is a cat "  #单引号中间还有单引号，可以转义
print(sentence)
sentence2 = "tom's pet is a cat "  #也可以用双引号包含单引号
print(sentence2)
sentence3 = "tom said:\"hello world!\""
print(sentence3)
sentence4 = 'tom said:"hello world!"' #三个连续的单引号或双引号，可以保存输入格式，允许输入多行字符串
print(sentence4)
worlds = """
hello
world
abcd """
print(worlds)

py_str = "python "
len(py_str) 
print(py_str[0])
print('python'[0])
print(py_str[-1])
# py_str[7]  错误 ，下标超出范围
print(py_str[2:4])
print(py_str[2:]) #从下标为2得字符取到结尾
print(py_str[:2]) #从开头取到下标是2之前得字符
print(py_str[:])  #取全部
print(py_str[::2]) #步长值为2，默认是1
print(py_str[1::2])
print(py_str[::-1]) #步长为负，表示自右向左取

print(py_str + ' is good') #简单得拼接到一起
print(py_str * 3 ) #把字符串重复3便

print('t' in py_str)  #true
print("th" in py_str)  #true
print("to" in py_str)   #false
print("to" not in py_str) #true
