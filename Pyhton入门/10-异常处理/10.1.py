# 简单异常处理
# 给出提示信息

try:
    num = int(input("Please input your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(rst))

# 捕获异常后，把异常实例化，出错信息会在实例里
# 注意以下写法
# 以下语句是捕获ZeroDivisionError异常并实例化实例e
except ZeroDivisionError as e:
    print("nnnnnnnnnnn,哥屋恩")
    print(e)
    exit()  # exit是退出程序的意思

# 如果是多种error的情况
# 越具体的错误，越往前放
# 在异常类继承关系中，越是子类的异常，越要往前放
# 越是父类的异常，越要往后放
except NameError as e:
    print("名字起错了")
    print(e)
    exit()
except AttributeError as e:
    print("属性有问题")
    print(e)
    exit()

# 所有异常都是继承自Exception
# 如果写上下面这句话，任何异常都会拦截住
except Exception as e:
    print("我不知道哪里出错了")
    print(e)