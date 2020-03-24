# a = ("hello", "你好", None,0, 90, 100,'')
# print(a[1])
# 切片
# print(a[1:])
# print(a[:4])
# print(a[:-2])
# print(a[1:4])  # 左闭右开

# print(a[None:])
# print(a.index("你好"))
# print(a.index(None))
# print(a.index(''))
# print(a.count("你好"))

# 二维元组
# b = (a,1111,2222)
# print(b[0][1])

# a = ["hello", "你好", None,0, 90, 100,'']
# a.append("append")
# a.insert(0,"插入")
# print(a)
# b = a.pop(3)
# c = a.pop(0)
# print(a+b)
# print(a)
# xx = ["您好",1] 
# a.extend(xx)
# print(a)
# a.sort()  # 排序，只能对数字进行排序
# print(a)

# a = {"name":"zhangsan", "age":"18"}
# 取值
# print(a["name"])
# 新增
# a["hight"] = "180"
# print(a)
# 修改
# a["name"] = "lisi"
# print(a)

# print(a.get("name"))
# print(a.pop("age"))
# a.update(age =22)
# print(a)


# 数组和字典删除
# del ap["name"]
# print(a)

# del a[0]

"""
练习：
    获取用户输入的个人信息，并且存到字典中
    个人信息包括了，姓名，年龄，和性别
"""
a = {}
name = str(input("请输入你的姓名："))
age = int(input("请输入你的年龄："))
sex = str(input("请输入你的性别："))
a["xing"] = name
a["age"] = age
a["sex"] = sex
print(a)




