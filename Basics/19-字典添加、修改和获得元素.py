# 字典查找效率比较高，但是比较占内存，字典以空间换时间。
# 字典使用{}，my_dict = {key1:val1,key2:val2}
# 注意，键是唯一的，值是可以重复的。如果键相同会替换前面的
def val1():
    my_dict = {'name':'王金龙','age':18,'sex':'男'}
    print(my_dict)

def val2():
    my_dict = {'name':'王','age':1,'sex':'男'}
    print(my_dict['name'])

def val3():
     my_dict = {'name':'王','age':1,'sex':'男'}
     my_dict['name'] = '金龙'# 如果key存在就是修改元素
     print(my_dict)
     my_dict['shengao'] = 175# 如果不存在就是天剑新元素
     print(my_dict)

val3()

