alist = [10,20,30,"bob","alice",[1,2,3]]
print(alist)
len(alist)
print(alist[-1]) #取出最后一项
print(alist[-1][-1]) #取出最后一项列表，再在列表取下标
print([1,2,3][-1]) 
print(alist[-2][2])
print(alist[3:5])
print(10 in alist) 
print("o" in alist)
print(100 not in alist) 
alist[-1] = 100   #修改最后一项得值
print(alist)
alist.append(200) #向列表中追加一项
print(alist)
alist += [25] #向列表中追加一项
print(alist)
