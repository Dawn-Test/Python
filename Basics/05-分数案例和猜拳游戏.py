# 根据分数显示档位
# 1，获得输入的分数
# 2，将分数从字符串类型转换为数字类型
# 3. 根据分数分档
#     3.1  90-100  A档
#     3.2  80-90   B档
#     3.3  70-80   C档
#     3.4  60-70   D档
#     3.5  60以下  E档

# 获得用户输入的分数
# seore = float(input('请输入分数：'))
#
#
# if seore >=90 and seore <= 100 :
#     print('成绩为A档')
# elif seore >=80 and seore < 90 :
#     print('成绩为B档')
# elif seore >=70 and seore <80 :
#     print('成绩为C档')
# elif seore >=60 and seore <70 :
#     print('成绩为D档')
# elif seore <60:
#     print('成绩为E档')
# else:
#     print('成绩输入错误！')

#猜拳游戏
# 1.获得用户输入的石头、剪刀、布
# 2，电脑产生一个石头（0）、剪刀（1）、布（2）
# 3，判断胜负
import random  #随机导入
# 输入猜拳
user_quan = int(input('请出拳 石头（0）、剪刀（1）、布（2）:'))
# 随机产生0-2之间的整数
computer = random.randint(0,2)   #randint随机冲0-2取出一个数字
# 判断玩家胜负
if ((user_quan == '0') and (computer == '2')) or ((user_quan == '1') and (computer == '0'))  or ((user_quan == '2') and (computer == '1')):
    print('你赢了！')
elif user_quan == computer:
    print('平局！')
else:
    print('你输了！')









