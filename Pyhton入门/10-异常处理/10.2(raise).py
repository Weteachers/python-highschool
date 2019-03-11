# raise案例-1

class TTValueError(ValueError):
    pass
try:
    print("我爱TTTTTTTT")
    print(2222222)
    # 手动引发一个异常
    # 注意语法：raise ClassName
    raise ValueError
    print("Hold on")

except NameError as e:
    print("NameError")

except ValueError as e:
    print("ValueError")

except Exception as e:
    print("有异常")

finally:
    print("我肯定会被执行。。。")