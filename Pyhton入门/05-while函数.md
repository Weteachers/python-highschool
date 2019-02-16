# while循环
- 一个循环语句
- 表示当某条件成立的时候，就循环
- 不知道具体循环次数，但能确定循环的成立的条件的时候用while循环
- while语法：
        
        while 条件表达式：
            语句块
        #另外一种表达方法
        while 条件表达式：
            语句块1
        else：
            语句块2
# 函数
- 代码的一种组织形式
- 一个函数一般完成一种特定的功能
- 函数使用
    - 函数需要先定义
    - 使用函数，俗称调用
### 函数的参数和返回值
- 参数：负责给函数传递一些必要的数据或者信息
- 返回值：函数的执行结果
    - 使用return关键字
    - 如果没有return，默认返回一个None
    - 函数一旦执行return语句，结束函数的执行
    

    # 参数的定义和使用
    def hello(person):
        print("{0},你怎么了".format(person)) # 注意format的用法
        print("Sir,你这就走了")
    p = "明月"
    hello(p)
## 参数详解
- [参考资料](https://www.cnblogs.com/bingabcd/p/6671368.html)
- python参考资料： headfirst python -> 零基础入门学习python（小甲鱼），本讲义参考的是流畅的python -->习题-->后期可以考虑腾讯免费公开课
- 参数分类
    - 1.普通参数
    - 2.默认参数
    - 3.关键字参数
    - 4.收集参数
- 1.普通参数
    - 参见上例
    - 定义的时候直接定义变量名
    - 调用的时候直接把变量或者值放入指定位置
            

        def 函数名(value1,value2):
    函数体
    # 调用
    函数名(value1,value2,value3)
    #调用的时候，具体值参考的是位置，按位置赋值

- 2.默认参数
    - 形参带有默认值
    - 调用的时候，如果没有对相应形参赋值，则使用默认值
                

        def  func_name(p1=v1, p2=v2,...):
            func_block
    #调用1
    func_name()
    #调用2
    value1=100
    value2=200
    func_name(value1,value2)
    
- 3.关键字参数
    - 语法
    
            def func(p1=v1,p2=v2,...):
                func_body
            # 调用函数：
            func(p1=value1, p2=value2...)
            
            
    - 比较麻烦，但也有好处：
        - 不容易混淆，一般实参和形参只是位置一一对应即可，容易出错
        - 使关键字参数，可以不考虑参数位置
        

                # 关键字参数案例
                def stu_key(name="No name",age=0, addr="No addr"):
                    print("I am a student.")
                    print("我叫{0}, 我今年{1}岁了，我住{2}".format(name,age,addr))
                name = "tc"
                age = 18
                addr = "bnu"
                # 普通参数，只按照位置传递，容易出错
                stu_key(name=name,age=age, addr=addr)
- 4.收集参数
    - 把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
    - 语法：
    
    ```
    def func(*args):  
        func_body  
        按照list使用方式访问args得到传入的参数  
    调用：  
        func(p1, p2, p3,...)
    ```
    - 参数名args不是必须这么写，但是，我们推荐使用args，约定俗成
    - 参数名args前需要有星号
    - 收集参数可以和其他参数共存
    ```
    # 收集参数代码  
    # 函数模拟一个学生进行自我介绍，但具体内容不清楚
    # args把他看做一个list
    def stu(*args):
        print("hello，请允许我自我介绍一下：")
        # type函数的作用是检测变量的类型
        print(type(args))
        for item in args:
            print(item)
    stu("tc", 18, "Beijing", "z", "single")
    stu("大神")
    ```
    - 如果使用关键字参数格式调用，会报错  
    stu(name="tc")
    - 收集参数之关键字收集参数
        - 把关键字参数按字典格式存入收集参数
        - 语法：
        ```
        def func(**kwargs):
            func_body
        # 调用：
        func(p1=v1, p2=v2, p3=v3...)
        ```
        - kwargs一般约定俗成
        - 调用的时候，把多余的关键字参数放入kwargs
        - 访问kwargs需要按字典格式访问
        ```
        # 收集参数案例
        # 自我介绍
        # 调用的时候需要使用关键字参数调用
        def stu(**kwargs):
            # 在函数体内对于kwargs的使用不用带星号
            print("Hello 大家好，我自我介绍一下：")
            print(type(kwargs))
            # 对于字典的访问，python2 和python3 有区别
            for k,v in kwargs.items():
                print(k, "---", v)
        stu(name="tc", age=18, addr="Beijing", lover="z")
        print("*"*20)  #这个小技巧is nice
        stu(name="God")
        stu()  #参数为空也没毛病
        ```
    - 收集参数混合调用的顺序问题
        - 收集参数，关键字参数，普通参数可以混合使用
        - 使用规则，普通参数和关键字参数优先
        - 定义的时候一般找普通参数，关键字参数，收集参数tuple，收集参数dict
        ```
        # 收集参数 混合使用调用案例
        # stu模拟一个学生的自我介绍
        def stu(name, age,  *args, hobby="没有", **kwargs):
            print("hello大家好")
            print("我叫{0},我今年{1}了".format(name,age))
            if hobby=="没有":
                print("我没有爱好，很遗憾")
            else:
                print("我的爱好是{0}".format(hobby))
            print("*" *20)
            for i in args:
                print(i)
            print("&" *30)
            for k,v in kwargs.items():
                print(k, "---", v)
        # 开始调用函数
        name = "tc"
        age = 18
        
        # 多种调用方式
        stu(name,age)
        stu(name,age,hobby="游泳")
        stu(name, age, "z", "tc", hobby="游泳", hobby2="学习", hobby3="继续学习")
        ```
    - 收集参数的解包问题
        - 把参数放入list，直接把list/dict  中的值放入收集参数中
        - 语法：参考案例：
        ```
        def stu(*args):
            print("hello world")
            n = 0
            for i in args:
                print(type(i))
                print(n)
                n = n+1
                print(i)
        l = ["tc", 18, 18, "z"]
        stu(l)
        # 此时，args的表示形式是字典内一个list类型的元素，即args = (["tc", 18, 18, "z"])
        # 很显然，与我们的最初想法违背
        
        # 此时的调用，我们就需要解包符号，即调用的时候前面加一个星号
        stu(*l)
        ```
        - 同理，dict类型收集参数一样可以解包，但是
            - 对dict进行解包，需要**两个星号**进行解包
## 返回值
- 函数和过程的区别
    - 有无返回值
- 需要用return显示返回内容
- 如果没有返回，则默认使用None
- 推荐写法，无论有无返回值，最后都以return结束
# 函数文档
函数的文档的作用是对当前函数提供使用相关的参考信息
- 文档的写法：
    - 在函数内部开始的第一行使用三引号字符串定义符
    - 一般具有特定格式
    - 详情参考案例：
- 文档查看方法
    - 使用help函数，形如  **help(func)**
    - 使用doc, 参看案例（更干净一点）
    ```
    # 文档案例
    # 函数stu是模拟一个学生的自我介绍的内容
    def stu(name, age, *args):
        '''
        这是第一行
        这是第二行
        这是第三行
        '''
        print("This is func_stu")
    help(stu)
    print("&" *20)
    print(stu.__doc__)
    ```
## 传值和传地址的区别
- 对于简单的数值，采用传值操作，即在函数内部对参数的操作不影响外面的变量
- 对于复杂变量，采用传地址操作，此时函数内的参数和外部变量是同一份内容，任何地方对此内容的更改都影响另外的变量或参数的使用
```
def a(n):
    n[2] = 300
    print(n)
    return None
def b(n):
    n += 100
    print(n)
    return None
a1 = [1,2,3,4,5,6]
b1 = 9

print(a1)
a(a1)
print(a1)

print(b1)
b(b1)
print(b1)
```
```
# 上述代码运行结果：
[1, 2, 3, 4, 5, 6]
[1, 2, 300, 4, 5, 6]
[1, 2, 300, 4, 5, 6]
9
109
9
```
    