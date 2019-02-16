# 变量作用域
- 变量有作用范围限制
- 分类
    - 全局（global）：在函数外部定义
    - 局部（local）：在函数内部定义
- 变量的作用范围：
    - 全局变量：在整个全局范围都有效
    - 全局变量在局部可以使用（即函数内部可以访问函数外部定义的变量）
    - 局部变量在局部范围可以使用
    - 局部变量在全局范围无法使用
- LEGB原则
    - L（local）局部作用域
    - E（Enclosing function locale）外部嵌套函数作用域
    - G（Global module）函数定义所在模块作用域
    - B（Buildin）：python内置模块的作用域
- 局部变量升级为全局变量
    - 使用global

## globals, locals函数
- 可以通过globals和locals函数显示出局部变量和全局变量
- globals 和 locals 叫做内建函数
- 参考以下案例
    ```
    a=1
    b=2
    def fun(c,d):
        e=3
        print("Locals={0}".format(locals()))
        print("Globals={0}".format(globals()))
    fun(4,5)
    ```
## eval()函数
- 把一个字符串当成一个表达式来执行，返回表达式执行后的结果
- 语法：
    -eval(string_code, globals=None, locals=None)
    ```
    x = 1
    y = 1 
    z = x + y
    zz = eval("x+y")
    print(z)
    print(zz)
    ```
## exec()函数
- 跟eval功能相似，但是，不返回结果
- 语法：
    - exec(string_code, globals=None, locals=None)
    ```
    x = 1
    y = 2
    # 执行x+y
    # z=x+y
    z1 = x + y
    # 1.注意字符串中引号的写法
    # 2.比对exec执行结果和代码执行结果
    z2 = exec("print('x+y:',x+y)")
    
    print(z1)
    print(z2)
    ```
# 递归函数
- 函数调用自己
- 优点：简洁，理解容易
- 缺点：对递归深度有限制，消耗资源大
- python对递归深度有限制，超过限制会报错
- 在写递归程序的时候，注意递归出口
    ```
    # 递归调用深度限制代码
    x = 0
    def fun():
        global x
        x += 1
        print(x)
        fun()
    fun()
    ```
- 例1：斐波那契数列
    - f(1)=1,f(2)=1,f(n)=f(n-1)+f(n-2)
    ```
    def fib(n):
        if n==1:
            return 1
        elif n==2:
            return 1
        return fib(n-1)+fib(n-2)
    print(fib(10))
    print(fib(20))
    ```
- 例2：汉诺塔
    - 规则：
        - 1.每次移动一个盘子
        - 2.任何一次移动，三个塔的状态必须是小盘在上，大盘在下
    - 方法：
        - 1.n=1: 直接把A上的一个盘子移动到C上，A->C
        - 2.n=2：
            - A.把小盘子从A放到B上，A->B
            - B.把大盘子从A放到C上，A->C
            - C.把小盘子从B放到C上，B->C
        - 3.n=3:
            - A.把A上的两个盘子，通过C移动到B上去，调用递归实现
            - B.把A上剩下的一个最大盘子移动到C上，A->C
            - C.把B上的两个盘子，借助于A，挪到C上去，调用递归
        - 4.n=n:
            - A.把A上的n-1个盘子，借助于C，移动到B上去，调用递归
            - B.把A上的最大盘子，也是唯一一个，移动到C上，A->C
            - C.把B上的n-1个盘子，借助于A，移动到C上，调用递归
    ```
    def hano(n, a, b, c):
        '''
        汉诺塔的递归实现
        n: 代表几个盘子
        a: 代表第一个塔，起点
        b: 代表第二个塔，中间过渡作用
        c: 代表第三个塔，目标塔
        '''
        if n==1:
            print(a,"-->",c)
            return None
        if n==2:
            print(a,"-->",b)
            print(a,"-->",c)
            print(b,"-->",c)
            return None
        # 把n-1个盘子，从a塔移动到b塔，借助c
        hano(n-1, a, c, b)
        print(a,"-->",c)
        # 把n-1个盘子，从b塔移动到c塔，借助a
        hano(n-1, b, a, c)
    a = "A"
    b = "B"
    c = "C"
    
    n=10
    hano(10,a,b,c)
    ```
    
    