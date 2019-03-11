# 生成列表的两种方法的比较
# 如果单纯比较生成一个列表的时间，可能很难实现
import timeit
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''

# 利用timeit调用代码，执行100000次，查看运行时间
t1 = timeit.timeit(stmt = "[i for i in range(1000)]", number = 100000)
# 测量代码c执行100000次运行的结果
t2 = timeit.timeit(stmt=c, number=100000)
print(t1)
print(t2)