# return：函数返回值
# 函数执行到return时：立刻终止函数。一个函数可以有多个return！
def  my_add(a,b):
    ret = a+b
    return ret

# 保存函数的返回结果
ret =my_add(10,20)
# 使用函数计算的结果，进行下一步计算
final_result = ret +100
# 输出最终结果
print ('最终结果',final_result)

# print是一个函数，只是一个功能，return是一个语句，和def if类似。
# print会把结果打印在屏幕上，return把结果返回下一步。