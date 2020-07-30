# 1.小明爱跑步
# 需求：小明体重15.0公斤，小明没吃跑步减肥0.5公斤，每次吃东西体重增加1公斤
# class Person :
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#
#     def __set__(self):
#         return '我的名字叫%s体重是%.2f公斤' % (self.name,self.weight)
#     def run(self):
#         print('%s爱跑步，跑步锻炼身体'% self.name)
#     def eat(self):
#         print('%s 是吃货，吃完这顿再减肥' % self.name)
# xiaoming = Person('小明',75.0)
#
# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)
#

# 摆放家具
# 需求：有户型、总面积和家具名称列表
# 家具有名字和占地面积，其中席梦思 4平米、衣柜2平米、餐桌1.5平米
# 将三个添加到房子中
# 打印房子,要求输出房型.总面积.剩余面积.家具名称列表

class HouseItem:

    def __index__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name,self.area)
class House:
    def __index__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []
    def __str__(self):
        return "户型：%s\n总面积：%.2f[剩余：%.2f]\n 家具：%s" \
               % (self.house_type,self.area,
                  self.free_area,self.item_list)
# 1.创建家具
bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)

print(bed)
print(chest)
print(table)

# 创建房子对象
my_house =  House('两室一厅',60)

my_house.add_item(bed)
print(my_house)