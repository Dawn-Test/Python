# 文件重命名

import os
def chongmingming():
    os.rename('a.txt','hello.txt')

chongmingming()

#文件删除

import os
def  shanchu():
    os.remove('a.txt')
shanchu()
# 路径问题，如果只写文件名，默认当前目录找文件，如果找不到就报错
# 可以在a.txt前面添加文件路径，进行删除

# 创建和删除目录（文件夹）
import os
def wenjianjia():
    os.mkdir('/users/***')   # 创建文件夹
    os.rmdir('/users/***')    #删除文件夹
wenjianjia()

# 获取指定目录下的文件列表
def  huoqu():
    content = os.listdir()
    print(content)

# 获得和设置工作目录
def shezhi():
    cwd = os.getcwd()
    # cwd  current（当前的） working（工作） directory（）目录
    print(cwd)
shezhi()           # 获取当前文档目录路径