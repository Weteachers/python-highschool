# getcwd() 获取当前的工作目dd录
# 格式：os.getcwd()
# 返回值：当前工作目录的字符串
# 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
import os
mydir = os.getcwd()
print(mydir)

# chdir() 改变当前的工作目录
# change directory
# 格式：os.chdir(路径)
# 返回值：无
# os.chdir('F:/Python/python_highschool/Python入门')
mydir = os.getcwd()
print(mydir)

# listdir() 获取一个目录中所有子目录和文件的名称列表
# 格式：os.listdir(路径)
# 返回值：所有子目录和文件名称的列表
ld = os.listdir()
print(ld)

# makedirs() 递归创建文件夹
# 格式：os.makedirs(递归路径)
# 返回值：无
# 递归路径：多个文件夹层层包含的路径就是递归路径   例如 a/b/c
rst = os.makedirs("tt")
print(rst)

# system() 运行系统shell命令
# 格式：os.system(系统命令)
# 返回值：打开一个shell或者终端界面
# 一般推荐使用 subprocess 代替
# ls是列出当前文件和文件夹的系统命令
rst = os.system("ls")
print(rst)
# 在当前目录下创建一个tt.hh的文件
rst = os.system("touch rst.hh")
print(rst)

# getenv() 获取指定的系统环境变量值
# 相应的还有 putenv
# 格式：os.getenv('环境变量名')
# 返回值：指定环境变量名对应的值
rst = os.getenv("PATH")
print(rst)

# exit() 退出当前程序
# 格式：exit()
# 返回值：无





