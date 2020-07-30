# input_content = input('请输入你的尊姓大名：')
# print('欢迎您 %s !' % input_content)
#返回结果为：欢迎您***！

#
# gongshi = input('请输入你的公司：')
# name = input('请输入你的姓名：')
# tel = input('请输入你的电话：')
# youxiang = input('请输入你的邮箱：')
#
# print('*'*50)
# print('公司：%s' % gongshi)
# print()
# print('姓名：%s'% name)
# print()
# print('电话：%s'% tel)
# print()
# print('邮箱: %s' % youxiang)
# print('*'*50)
# 输出结果：
# **************************************************
# 1
#
# 姓名：王金龙
#
# 电话：466656
#
# 邮箱: 33@qq.c
# **************************************************

left_num = input('请输入第一个数字：')
right_num = input ('请输入第二个数字：')

# 由于各种原因我们得到的数字不是想要的类型，所以需要类型转换
# int(a),将a变量转换为int类型。数字
# float(a),将a变量转换为float类型。
# str(a),将a变量转换为str类型。
left_num_int = int(left_num)
right_num_int = int(right_num)

#进行加法运算
resuit = left_num_int + right_num_int

print('%d + %d 的结果是 %d' %(left_num_int , right_num_int,resuit))
