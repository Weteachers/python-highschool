import timeit
def doIt():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))

# 执行函数，重复10次
t = timeit.timeit(stmt = doIt, number=10)
print(t)

s = '''
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
'''
# 执行doIt(num)
# setup负责把环境变量准备好
# 实际上相当于给timeit创造了一个小环境
t = timeit.timeit("doIt(num)", setup=s+"num=3", number=10)
print(t)