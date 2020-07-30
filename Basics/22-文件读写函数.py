# 写文件：write  writelines
#
# def test01():
#     # 写操作
#     f = open('a.txt','w')
#     # write 一次写入一行
#     f.write('hello.world!')
#     # writelines 一次写入多行，参数是一个列表，列表每一个元素都是一行数据
#     lines = ['aaa\n','bbb\n','ccc\n']
#     f.writelines(lines)
#     f.close()
#
# test01()

def test02():
    # 读操作
    f = open('a.txt','r')
    content = f.read(3)
    print(content)
    f.close()

test02()