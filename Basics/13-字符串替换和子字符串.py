a = '横看成岭侧成峰，远近高低各不同。不'

# replace 并不会替换原来的字符串，替换完毕返回一个新的字符串！
new_a = a.replace('不','相')  # 如果后面不加1，则替换所有的字符
print(a)
print(new_a)

new_a = a.replace('不','相',1)
print(new_a)

# 容器的专属方法（函数）
# 字符串通过点的方式调用专属的函数

# 子字符串：
# a = 'wangjinlong@QQ，com'
# 1，找到字符串中@的位置
# 2.获取字符串中的字串

a = 'wangjinlong@QQ，com'
# 如果查到，返回字串第一次出现的位置
# 如果查不到@，返回 -1
b = a.find('@')
if a == -1:
    print('@不存在，邮箱不合法！')
else:
    print('@的位置是:',b)

