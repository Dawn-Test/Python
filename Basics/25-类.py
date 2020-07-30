#  1.在python 中定义一个只包含方法的类
# 类名满足大驼峰命名法：每一个单词首字母大写！！
# 第一个参数必须是self ！！！
# class 类名 ：
#    def 方法1（self，参数列表）：
#    pass
#    def 方法2（self，参数列表：）
#     pass

# 2.当一个类定义完成后，要使用这个类来创建对象！
# 对象变量 = 类名（）

# 第一个面向对象程序：
# 需求
#    小猫要吃鱼，小猫要喝水
# 分析
# 1.定义一个猫类cat
# 2.定义两个方法eat和drink
# 3.按照需求————不需要定义属性
class Cat :
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print('%s 爱吃鱼'% self.name)
    def drink(self):
        print('%s 要喝水'% self.name)

# 创建猫对象
tom = Cat()
# 加属性，使用 .属性名  利用赋值语句
tom.name = 'tom'

# 调用方法
tom.eat()
tom.drink()
# print(tom)   #  输出对象

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = '大懒猫'
lazy_cat.eat()
lazy_cat.drink()
# print(lazy_cat)

# 类只有一个，他两不是同一个

# 初始化方法

class Cat:
    def __init__(self):
        print('初始化方法')
        self.name = 'tom'
tom = Cat()
print(tom.name)