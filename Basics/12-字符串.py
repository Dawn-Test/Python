# 1、字符串定义
my_str = 'hello'
# my_str = """你好吗
#             我很好
# """
# print(my_str)
# 遍历：不重复的访问容器中的每一个元素。

print(my_str[0])  # 0是索引，小标
print(my_str[-1])

i = 0
while i <5:
    print(my_str[i],end=' ')  # 不加end+=‘’，就是以列的形式显示
    i +=1
print()

for a  in my_str: # for循环
    print(a ,end='')  # 不加end+=‘’，就是以列的形式显示