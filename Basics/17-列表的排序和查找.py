# sort()  排序
# 创建一个包含10个随机数的列表
import random
my_list = []
i = 0
while i <10:
    # 产生随机数
    random_number = random.randint(1,100)
    # 将随机数插入列表中
    my_list.append(random_number)
    i += 1
print(my_list)
# 对列表中的随机数进行排序 sotr 排序
my_list.sort()
print(my_list)
# 将 sort 函数的 reverse 默认值改成 true 实现实现从大到小排序
my_list.sort(reverse=True)
print(my_list)
# 逆序
my_list.remove()
print(my_list)


# 列表的查找：index（）

my_list = [1,2,3,4,5]
a = 1
b = 200
# index 用于根据值查询，如果查询失败，则会报错
if a in my_list:
    # 查找值为 a 的位置
    pos = my_list.index(a)
    # 根据位置修改值
    my_list[pos] = b
print(my_list)
