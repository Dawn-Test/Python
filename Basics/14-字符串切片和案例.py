a = 'wangjinlong@QQ，com'

print(a[0])
print(a[0:5])
# 获取容器元素的个数
b = len(a)
print(a[12:b])

# 起始值不写表示从零开始
print(a[:12])
# 结束值不写表示到最后
print(a[12:])
print(a[:])
# 步长
print(a[0:12])
print(a[0:12:3])

# 了解 起始 结束 步长都可以是负数
print(a[-5:-1])
#
print(a[6:1:-1])
# 字符串逆序
print(a[::-1])


# 邮箱案列：
a = 'wangjinlong@QQ，com'

b = a.find('@')
if a == -1:
    print('@不存在，邮箱不合法！')
else:
    username = a [:b]
    houzhui = a [b+1:]
    print('用户名是：',username)
    print('邮箱后缀：',houzhui)

# split拆分符：
a = 'wangjinlong@QQ，com'
result = a.split('@')
# 获取@个数
if result > 1:
    print('你的邮箱不合法！')
else:
    print('用户名是：', result[0])
    print('邮箱后缀：', result[1])

# 注册案例
username = input('请输入你要注册的用户名：')

new_username = username.strip()
# strip 函数默认去除字符串两边的空格
if new_username.isalpha():
# isalpha 函数 判断字符串所有的袁术是否为字母
    print('注册成功！')
else:
    print('注册失败！')

# username.isdigit() 判断是否为数字
