yuangongs = {}

def show_menu():
    print('*'*20 + '员工管理系统菜单'+ '*'*20)
    print('1.添加员工信息')
    print('2.删除员工信息')
    print('3.修改员工信息')
    print('4.显示员工信息')
    print('5.退出管理系统')
    print('*'*48)

def add_new_yuangong():
    """"添加员工信息"""
    yuangong_id = input('请输入员工编号：')
    # 判断员工号是否存在
    all_yuangong_id = list(yuangongs.keys())
    if yuangong_id in all_yuangong_id:
        print('员工号重复，添加失败！')
        return
    # 如果不重复进行以下操作
    yuangong_name = input('请输入员工姓名：')
    yuangong_sex = input('请输入员工性别：')
    yuangong_salary = input('请输入员工的工资：')

    yuangong_info = {'name':yuangong_name,'sex':yuangong_sex,'salary':yuangong_salary}
    yuangongs[yuangong_id] = yuangong_info
    print('员工编号为 %s 的员工信息添加成功' % yuangong_info)

def remove_yuangong():
    # 获得要删除的员工编号
    yuangong_id = input('请输入要删除的员工编号：')
    # 如果员工号不存在的话，提示错误信息，终止函数执行
    all_yuangong_id = list(yuangongs.keys())
    if yuangong_id  not in all_yuangong_id:
        print('员工编号不存在，添加失败！')
        return
    # 如果存在删除对应的信息
    del yuangongs[yuangong_id]
    print('员工编号为 %s 的员工信息删除！' % yuangong_id)


def edit_yuangong():
    yuangong_id = input('请输入要修改的员工编号：')

    all_yuangong_id = list(yuangongs.keys())
    if yuangong_id  not in all_yuangong_id:
        print('员工编号不存在，修改失败！')
        return
    new_yuangong_name = input('姓名：%s,您要修改为：' % yuangongs[yuangong_id]['name'])
    new_yuangong_salary = input('工资：%s,您要修改为：' % yuangongs[yuangong_id]['salary'])
    new_yuangong_sex = input('性别：%s,您要修改为：' % yuangongs[yuangong_id]['sex'])
    if new_yuangong_name != '':
         yuangongs[yuangong_id]['name'] = new_yuangong_name
    if new_yuangong_sex != '':
         yuangongs[yuangong_id]['sex'] = new_yuangong_sex
    if new_yuangong_name != '':
         yuangongs[yuangong_id]['salary'] = new_yuangong_salary
    print('员工编号为：%s 的员工信息修改成功！' % yuangong_id)

def show_yuangong():
    for yuangong in yuangongs.items():
        print('%s\t\t%s\t\t%s\t\t%s' % (yuangong[0],yuangong[1]['name'],yuangong[1]['sex'],yuangong[1]['salary']))


while True:
    show_menu()
    my_operate = input('请输您的操作:')
    if my_operate == '1':
        add_new_yuangong()
        print(yuangongs)
    elif my_operate == '2':
        remove_yuangong()
    elif my_operate == '3':
        edit_yuangong()
    elif my_operate == '4':
        show_yuangong()
    elif my_operate == '5':
        print('退出系统')
        break # 退出
    else:
        print('您的输入有误')