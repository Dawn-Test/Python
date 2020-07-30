# 函数的好处：减少代码的书写。减少维护量，功能的封装。降低学习成本，提升开发速度。
# def 函数名（）：
#      一行或多行代码，缩进！
# 定义的函数只能在本页面使用！

# 例：打印星星
def xingxing():
    a= 1
    while a <=5:
        print('*'*a)
        a +=1
xingxing()  #调用函数。且函数必须要调用才能执行，调用几次打几次！
xingxing()


def  my_add():
    a=10
    b=20
    ret = a+b
    print('a+b=',ret)
my_add()

# 函数的参数：
def  my_add(a,b):
    ret = a+b
    print('a+b=',ret)

my_add(1,5)
my_add(10,60)  #位置参数，根据位置传递参数！
my_add(a=100,b=200) #关键字参数，可以不根据文字传递参数！
my_add(b=100,a=200)
# 1,5,10,60都是实参，a，b是形参

