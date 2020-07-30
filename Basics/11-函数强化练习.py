# 1.累加start到end的和
# def lejiahe(start,end):
#     i = start
#     mt_sum = 0
#     while i <= end:
#         mt_sum += i
#         i +=1
#     return mt_sum
# # 定义一个新的变量保存函数的返回结果
# ret = lejiahe(1,100)
# print('ret:',ret)

# 2、编写一个函数根据传入的运算符，进行相应的加减乘除 运算

def my_caculatal(left,right,operator):

    a = left
    b = right
    if operator == '+':
        ret = a + b
    elif operator == '-':
        ret = a - b
    elif operator == '/':
        ret = a / b
    elif operator == '*':
        ret = a * b
    else:
        print('输入错误！')
        ret = None  #表示什么都没有，在python中没有意义的值
    return ret
ret = my_caculatal(1,3,'+')
print('ret', ret)
ret = my_caculatal(right=4,left=2,operator='/')
print('ret', ret)

