# continue: 跳过本次循环
#1-100整数相加，去除50
# a = 1
# b = 0
# while a<=100:
#     if a ==50:
#          continue
#     a += 1
# print('总和：',b)
#当执行到continue，后面的代码不执行。直接回到while重新判断
#跳过本次循环，但不是退出循环。只能写在循环里面！！！

# break 退出循环：
# print('循环开始！')
# a = 0
# while a <= 100:
#     if a > 50:
#         break#当a>50时：就不再执行。退出循环！
#     print(a)
#     a += 1

# 3.while循环里面再次whlie循环：
# a = 0
# while a<3:
#     b = 0
#     while b <3:
#         if b ==2:
#             continue  #只能跳过本层循环的本次循环
#         print(b)
#         b +=1
#     a +=1

