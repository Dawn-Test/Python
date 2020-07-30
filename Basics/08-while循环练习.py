# 练习：简易版的员工管理系统
# 1.接受用户的输入
# 1.1输入1：展示所有员工的信息
# 1.2输入2：新增一个员工的信息
# 1.3输入3：修改一个员工的信息
# 1.4输入4：删除一个员工的信息
# 1.5输入5：退出员工管理系统

# print('欢迎您使用【员工管理系统1.0】')
# while True:
#     print('*'*10 + '操作菜单' + '*'*10)
#     print('1.展示所有员工信息')
#     print('2.新增所有员工信息')
#     print('3.修改所有员工信息')
#     print('4.删除所有员工信息')
#     print('5.退出所有员工信息')
#     print('*'*20)
#     user_operation = int(input('请输入您的操作：'))
#     if user_operation == 1:
#         print('姓名\t年龄\t性别')
#         print('小丽\t18\t女')
#         print('小龙\t21\t男')
#         print('小花\t19\t女')
#     elif user_operation ==2:
#         name = input('请输入新员工的姓名：')
#         age = input('请输入新员工的年龄：')
#         sex = input('请输入新员工的性别：')
#         print('新员工 %s 添加系统成功！' % name)
#     elif user_operation == 3:
#         name = input('请输入要修改员工的姓名：')
#         print('员工 %s 信息修改成功'% name)
#     elif user_operation == 4:
#         name = input('请输入要删除员工的姓名：')
#         print('员工 %s 信息删除成功')
#     elif user_operation == 5:
#         print('退出系统成功！')
#         print('欢迎再次使用本系统！')
#         break
#     else:
#         print('输入信息有误！')


#猜拳游戏循环玩
import random  # 随机导入
while True:
    user_quan = int(input('请出拳 石头（0）、剪刀（1）、布（2）:'))
    if user_quan ==3:
        print('退出系统！')
        break
    # 随机产生0-2之间的整数
    computer = random.randint(0,2)   #randint随机冲0-2取出一个数字
    # 判断玩家胜负
    if (user_quan == '0' and computer == '2') or \
            (user_quan == '1' and computer == '2') or \
            (user_quan == '2'and computer == '0'):
        print('你赢了！')
    elif user_quan == computer:
        print('平局！')
    else:
        print('你输了！')
