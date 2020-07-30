# if elif else
# 运算符：
# == 是否相等  ！=是否不等于  >是否大于  <是否小于  >=是否大于等于  <=  是否小于等于
# 如果成立返回true 不成立返回false
# 练习：登录页面

input_username = input('请输入您的用户名：')
input_password = input('请输入您的密码：')

correct_urername = 'admin'
correct_password = '123456'

# 首先判断用户名是否正确
if input_username == correct_urername:
    # 如果用户名正确，再判断密码是否正确
    if input_password == correct_password:
         print('欢迎 %s 登录系统' % input_username)
    else:
        print('您的用户名或密码错误！')
else:
    print('您的用户名或密码错误！')

#else： 后面不能加任何函数和命令










