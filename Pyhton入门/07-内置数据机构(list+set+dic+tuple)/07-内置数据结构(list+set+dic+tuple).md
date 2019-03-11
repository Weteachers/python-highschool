# 1.list（列表）
- 一组有顺序的数据的组合
- 创建链表
    ```
    # 1.创建空链表
    l1 = []
    # type是内置函数，负责打印出变量的类型
    print(type(l1))
    print(l1)
    
    # 2.创建有初值的列表
    l2 = [100]
    print(type(l2))
    print(l2)
    
    # 3.创建列表，带多个值
    l3 = [2,4,1,3,5,6]
    print(type(l3))
    print(l3)
    
    # 4.使用list()
    l4 = list()
    print(type(l4))
    print(l4)
    ```
## 列表常用操作
- 1.访问
    - 使用下标操作（索引）
    - 列表的位置是从0开始
    ```
    # 下标访问列表
    l = [3,4,2,5,1]
    print(l[3])
    ```
- 2.分片操作
    - 对列表进行任一段的截取
    - l[:]  # 左闭右开
    ```
    # 分片操作
    # 注意截取的范围
    print(l[1:4])
    
    # 下标值可以为空，如果不写，左边下标值默认为0，有边下标值为最大数加1，即表示截取到最后一个数据
    print(l[:])
    print(l[:4])
    print(l[2:])
    
    # 分片可以控制增长幅度，默认为1
    print(l[1:6])
    print(l[1:6:1])
    print(l[1:6:2])
    
    # 下标可以超出范围，超出后不再考虑超过的部分
    print(l[2:10])
    
    # 下标值、增长幅度可以为负数
    # 为负数，表面顺序是从右往左
    # 规定：数组最后一个数字的下标是-1
    
    # 下面显示的是空，因为默认分片总是从左往右截取
    print(l[-2:-4])
    
    # 正常情况下，分片左边的值一定小于右边的值
    print(l[-4:-2])
    
    # 如果非要左边值比右边大，则步长参数需要为负数
    # 此案例为一个list正反颠倒提供了一种思路
    print(l[-2:-4:-1])
    ```
    - 分片操作是生成一个**新的list**
        - 内置函数id，负责显示一个变量或者数据的唯一确定编号
        ```
        # id函数的案例
        a = 1
        b = 2
        print(id(a))
        print(id(b))
        
        c = a
        print(id(c))  # c和a的id值一样，说明它们是一个东西‘’
        # 如果a和c指向一份数据（确实如此），则更改a的值也会更改c的值
        # 但是，显示结果并非如此，为什么？？？
        ```
        ```
        l = [2,4,3,5,3,1]
        ll = l[:]
        lll = ll
        print(id(l))
        print(id(ll))
        print(id(lll))
        # 通过id知道，ll和lll是同一份数据，l和ll不是，因为“分片操作生成一个新的list”
        l[1] = 100
        print(l)
        print(ll)
        
        ll[1] = 100
        print(ll)
        print(lll)
        ```
- 3.del:删除命令
    ```
    # del删除
    a = [1,2,3,4,5,6]
    del a[2]
    print(a)
    ```
    ```
    # del删除 
    # 如果使用del后，id的值和删除前的不一样，则说明删除生成了一个新的list
    a = [1,2,3,4,5,6]
    print(id(a))
    del a[2]
    print(id(a))
    print(a)
    ```
    ```
    # del一个变量后不能再继续使用此变量
    del a
    print(a)   # 这是会报错的
    ```
- 4.列表相加
    - 使用加号连接两个列表
    ```
    a = [1,2,3,4,5]
    b = [6,7,8,9]
    c = ['a' , 'b', 'c']
    d = a + b + c 
    print(d)
    ```
    - 使用乘号操作列表
        - 列表直接跟一个列表接在一起
    ```
    # 列表直接跟一个整数相乘
    # 相当于把n个列表接在一起
    a = [1,2,3,4,5]
    b = a*3
    print(b)
    ```
- 5.成员资格运算
    - 判断一个元素是否在list里面
    - in
    ```
    a = [1,2,3,4,5,6]
    b = 8
    # c的值是一个布尔值
    c = b in a
    print(c)
    
    b = 4
    print(b in a)
    ```
    - not in
        - 和 in 类似
- 6.列表的遍历
    - for
    ```
    # for in list
    a = [1,2,3,4,5]
    for i in a:
        print(i)
    ```
    - while
        - 一般不用while遍历list
    ```
    a = [1,2,3,4,5]
    length = len(a)
    # index表示的是list的下标
    index = 0
    while index < length:
        print(a[index])
        index += 1
    ```
- 7.双层列表循环
    ```
    # a 为嵌套循环，或者叫做双层列表
    a = [["one", 1], ["two", 2],["three", 3]]
    for k,v in a:
        print(k, "--", v)
    ```
    ```
    # 双层列表循环变异
    a = [["one", 1, "enis"], ["two", 2, "zwei"], ["three", 3, "drei"]
    # 这个例子说明，k,v,w的个数应该跟解包出来的变量个数一致
    for k,v,w in a:
        print(k, "--", v, "--", w)
    ```
- 8.列表内涵：list content
    - 通过简单方法创作列表
    ```
    # for创建
    a = ['a', 'b', 'c']
    # 用列表a创建列表b
    # 下面代码的含义是，对于所有a中的元素，逐个放入新列表b中
    b = [i for i in a]
    print(b)
    ```
    ```
    # 对a中所有元素乘以10，生成一个新list
    a = [1,2,3,4,5]
    # 用list a创建一个list b
    # 下面代码的含义是，对于所有a中的元素，逐个放入新列表b中，不过这次要乘以110
    b = [i*10 for i in a]
    print(b)
    ```
    ```
    # 还可以过滤原来list中的内容并放入新列表
    # 比如原有列表a，需要把所有a中的偶数生成新的列表b
    a = [x for x in range(1, 35)]  # 生成从1到34的一个列表
    # 把a中的所有偶数生成一个新的列表b
    b = [m for m in a if m%2==0]
    print(b)
    ```
    ```
    # 列表生成可以嵌套
    # 有两个列表a, b
    a = [i for i in range(1,4)] #生成list a
    print(a)
    
    b = [i for i in range(100,400) if i%100 == 0]
    print(b)
    
    # 列表生成是可以嵌套，此时等于两个for循环嵌套
    c = [ m+n for m in a for n in b]
    print(c)
    
    #上面的代码和下面的效果很类似
    for m in a:
        for n in b:
            print(m+n, end="  ")
    # 嵌套的列表生成式也可以用条件表达式
    c = [ m+n for m in a for n in b if m+n <250]
    print(c)
    ```
### 列表常用的函数
- 1.len():
    - 列表的长度
    ```
    a = [x for in range(1,100)]
    print(len(a))
    ```
- 2.max():
    - 求列表中的最大值
print(max(a))
b = ['man', 'film', 'python']
print(max(b))

- 3.list():
    - 将其他格式的数据转换成list
    ```
    # 将list转换成list
    a = [1,2,3]
    print(list[a])
    
    # 将字符串转换成list（字符串的每个字符都被抽离，包括空格）
    s = "I love zz"
    print(list(s))
    
    # 把range产生的内容转换成list
    print(list(range(12, 19)))
    ```
- 4.append
    - 在列表末尾追加
    ```
    a = [ i for i in range(1, 5)]
    print(a)
    a.append(100)
    print(a)
    ```
- 5.insert(index, data)
    - 指定位置插入
    - insert(index, data),插入位置是index前面
    ```
    print(a)
    a.insert(3, 666)
    print(a)
    ```
- 6.pop
    - pop,从队尾拿出一个元素，即把最后一个元素取出来
    ```
    last_ele = a.pop()
    print(last_ele)
    print(a)
    ```
- 7.remove
    - 在列表中删除指定的值的元素
    - 如果被删除的值不在列表中，会报错
    - 所有需要进行先行判断
    ```
    if x in list:
        list.remove(x)
    ```
    ```
    # remove实例
    a.insert(4, 666)
    print(a)
    print(id(a))
    a.remove(666)
    print(a)
    print(id(a))
    # 输出两个id值一样，说明，remove操作是在原来list上直接操作
    ```
- 8.clear
    - 清空列表
    - 如果不需要列表地址保持不变，则清空列表可以使用以下方式 
        - a = list()
        - a = []
- 9.reverse
    - 翻转列表内容，原地翻转
    ```
    a = [1,2,3,4,5]
    print(a)
    print(id(a))
    
    a.reverse()
    
    print(a)
    print(id(a))
    ```
- 10.extend
    - 扩展列表：两个列表，把一个直接拼到后一个上
    ```
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    print(a)
    print(id(a))
    
    a.extend(b)
    print(a)
    print(id(a))
    ```
- 11.count
    - 查找列表中指定值或者说元素的个数
    ```
    print(a)
    a.append(8)
    a.insert(4,8)
    print(a)
    a_len = a.count(8)
    print(a_len)
    ```
- 12.copy
    - 拷贝，浅拷贝
    ```
    # 列表类型变量赋值示例
    a = [1,2,3,4,5,6]
    print(a)
    # list类型，简单赋值操作，是传地址
    b = a
    b[3] = 777
    print(a)
    print(id(a))
    print(b)
    print(id(b))
    # 上面的运行结果是，a和b的id值和内容都是一样一样的
    ```
    ```
    # 为了解决以上问题，list赋值需要采用copy函数
    b = a.copy()
    print(a)
    print(id(a))
    print(b)
    print(id(b))
    
    b[3] = 888
    print(a)
    print(b)
    ```
    ```
    ```
    ```
    # 深拷贝和浅拷贝的区别
    # 下列代码运行的运行结果产生的原因是，copy函数是个浅拷贝函数，即只拷贝一层内容
    # 深拷贝需要使用特定工具
    a = [1,2,3,[10,20,30]]
    b = a.copy()
    print(id(a))
    print(id(b))
    print(id(a[3]))
    print(id(b[3]))
    a[3][2] = 666
    print(a)
    print(b)
    
    # 上述代码运行结果如下：
    501155374216
    501155374024
    501155367688
    501155367688
    [1, 2, 3, [10, 20, 666]]
    [1, 2, 3, [10, 20, 666]]
    ```
    
# 2.元组-tuple
元祖可以看成是一个不可更改的list
## 2.1元组创建
```
# 创建空元组
t = ()

# 创建一个只有一个值的元组
t = (1,)  #要有逗号，不然t就成int型了
print(type(t))
t = 1,
print(type(int))
print(t)

# 创建多个值的元组
t = (1,2,3,4,5)
print(type(t))
print(t)
```
## 2.2元组的特性
- 是序列表，有序
- 元组数据值可以访问，不能修改，不能修改
- 元组数据可以是任意类型
- 总之，list所有特性，**除了可修改之外，元组都具有**
- 也就是说，list具有的一些操作，比如索引，分片，序列相加，相乘，成员资格操作等，一模一样
## 2.3元组相关的函数
- 1.len()
    - 获取元组的长度
- 2.max()  min()
    - 最大最小值；
    - 思考：如果列表或元组中有多个最大值，则实际打印出哪个
- 3.tuple
    - 转化或创建元组
    ```
    l = [1,2,3,4,5]
    t = tuple(l)
    print(t)
    
    t = tuple()
    print(t)
    ```
## 2.4元组的函数
基本跟list通用
- 1.count：计算指定数据出现的次数
    ```
    t = (2,1,2,4,3,2,5,4,1,4)
    print(t.count(2))
    ```
- 2.index：求指定元素在元组中的索引位置
    - 如果需要查找的数字是多个，则返回第一个
    ```
    # 接上面的代码
    print(t.index(1)
    ```
- 3.元组变量交换法
    - 两个变量交换值
    - 区别于C语言
    ```
    a = 1
    b = 3
    print(a)
    print(b)
    print("*" *20)
    # java程序员会这么写：
    c = a
    a = b
    b = c
    print(a)
    print(b)
    print("*" *20)
    # python的写法：
    a,b = b,a
    print(a)
    print(b)
    ```
# 3.集合set
集合是高中数学中的一个概念  
一堆确定的**无序**的**唯一**的数据，集合中每一个数据称为一个元素  
## 3.1 集合的定义
    ```
    s = set()
    print(type(s))
    print(s)
    # 此时，大括号内一定要有值，否则定义出的是一个dict
    s = {1,2,3,4,5,6}
    print(s)
    
    # 如果只用大括号定义，则默认是dict
    d = {}
    print(type(d))
    ```
## 3.2 集合的特征
- 1.  集合内数据无序，无法使用索引和切片
- 2.  集合内部数据元素具有唯一性，可以用来排除重复数据
- 3.  集合内的数据，str,int,float,tuple,冰冻集合等，即集合支持可哈希数据
    - 可哈希数据：如果一个对象在自己的生命周期中有一哈希值（hash   value）是不可改变的，那么它就是可哈希的（hashable）的，因为这些数据  结构内置了哈希值，每个可哈希的对象都内置了__hash__方法，所以可哈希  的对象可以通过哈希值进行对比，也可以作为字典的键值和作为set函数的参  数。所有python中所有不可改变的的对象（imutable objects）都是可哈希的，比如字符串，元组，也就是说可改变的容器如字典，列表不可哈希（unhashable）。我们用户所定义的类的实例对象默认是可哈希的（hashable），它们都是唯一的， 而hash值也就是它们的id
## 3.3 集合序列操作
- 1.成员检测 in/not in
    ```
    s = {4,5,"i","love","zz"}
    print(s)
    
    if "love" in s:
        print("哎呀")
    if "haha" not in s:
        print("爱个锤子")
    ```
- 2.遍历——for循环
    ```
    s = {4,5,"i","love","zz"}
    for i in s:
        print(i, end=" ")
    ```
- 3.带有元组的集合遍历
    ```
    s = {(1,2,3), ("i", "love", "zz"), (4,5,6)}
    for k,m,n in s:
        print(k, "--", m, "--", n)
    for k in s:
        print(k)
        
    # 运行结果：
    i -- love -- zz
    4 -- 5 -- 6
    1 -- 2 -- 3
    ('i', 'love', 'zz')
    (4, 5, 6)
    (1, 2, 3)
    ```
- 4.集合的内涵
    - 普通集合内涵
    ```
    s = {23,223,545,3,1,2,3,4,5,3,2,4,3}
    print(s)
    
    ss = {i for i in s}
    print(ss)
    ```
    - 带条件的集合内涵
    ```
    # 接上
    sss = {i for in s if i%2 == 0}
    print(sss)
    ```
    - 多循环的集合内涵
    ```
    s1 = {1,2,3,4}
    s2 = {"i", "love", "z"}
    
    s = {m*n for m in s2 for n in s1}
    print(s)
    
    # 运行结果：
    {'lovelove', 'love', 'lovelovelovelove', 'iiii', 'i', 'iii', 'zzzz', 'ii', 'zzz', 'zz', 'z', 'lovelovelove'}
    ```
## 3.4 集合相关的函数
- 1.len(),max(),min():跟list、tuple一样
- 2.set：生成一个集合
    ```
    l = [1,2,3,4,5,4,3,2,1]
    s = set(l)
    print(s)
    ```
- 3.add：向集合内添加元素
    ```
    s = {1}
    s.add(334)
    print(s)
    ```
- 4.clear:情况集合数据
    ```
    s = {1,2,3,4,5}
    print(id(s))
    s.clear()
    print(id(s))
    # clear前后你id值一样，结果表明clear函数是原地情况数据
    ```
- 5.copy：拷贝
- 6.remove和discard
    - remove：移除指定的值，直接改变原有值，如果要删除的值不存在，报错
    - discard：移除集合中指定的值，跟remove一样，但是如果要删除的话，不报错
    ```
    s = {23,3,4,5,3,1,2}
    s.remove(4)
    print(s)
    s.discard(1)
    print(s)
    print("*" * 20)
    
    s.discard(110)
    print(s)
    s.remove(110)
    print(s)
    
    # 思考：为啥remove不存在的值，会报“keyerror”？
    ```
- 7.pop：移除  
    - 随机移除一个元素
    ```
    s = {1,2,3,4,5,6}
    d = s.pop()
    print(d)
    print(s)
    ```
- 8.集合函数
    - intersection：交集
    - difference：差集
    - union：并集
    - issubset：检查一个集合是否为另一个子集
    - issuperset：检查一个集合是否为另一个集合的超集
    ```
    s1 = {1,2,3,4,5,6}
    s2 = {7,8,9,10}
    
    s_1 = s1.intersection(s2)
    print(s_1)
    
    s_2 = s1.difference(s2)
    print(s_2)
    
    s_3 = s1.issubset(s2)
    print(s_3)
    ```
- 9.集合的数学操作
    ```
    s1 = {1,2,3,4,5,6}
    s2 = {7,8,9,10}
    s_1 = s1 - s2
    ```
## 3.5 frozen set: 冰冻集合
- 冰冻集合，就是不可以进行任何修改的集合  
- 也是一种集合，是特殊的集合
```
# 创建
s = frozenset()
print(type(s))
print(s)
```
# 4.dict
- 字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现
## 4.1 字典的创建
    ```
    # 创建空字典法1
    d = {}
    print(d)
    
    # 创建空字典法2
    d = dict()
    print(d)
    
    # 创建有值的字典，每一组数据用冒号隔开，每一对键值对用逗号隔开
    d = {"one":1, "two":2, "three":3}
    print(d)
    
    # 用dict创建有内容字典
    d = dict({"one":1, "two":2, "three":3})
    print(d)
    
    # 用dict创建有内容字典法2
    d = dict([("one",1), ("two",2), ("three",3)])
    print(d)
    ```
## 4.2 字典的特征
- 字典是序列类型，没有分片和索引
- 字典中的数据每个都由键值对组成，即kv对
    - key：必须是可哈希的值，比如int，string，float，tuple，但是，list，set，dict不行
    - value：任何值
## 4.3 字典常见操作
- 1.访问数据
    ```
    d = {"one":1, "two":2, "three":3}
    # 注意访问方式，中括号内是键值
    print(d["one"])
    
    d["one"] = "eins"
    print(d)
    ```
    ```
    # 遍历在python2和python3中区别较大，代码不通用
    # 按key来使用for循环
    d = {"one":1, "two":2, "three":3}
    # 使用for循环，直接按key值访问
    for k in d:
        print(k, d[k])
    
    # 上述代码可以改写成如下（推荐）
    for k in.keys():
        print(k, d[k])
    # 只访问字典的值
     for v in d.values():
        print(v)
    
    # 注意以下特殊用法
    for k,v in d.items():
        print(k,'--',v)
    ```
- 2.del：删除
    ```
    del d["one"]
    print(d)
    ```
- 3.成员检测 in/ not in
    - 成员检测检测得是**key**的内容
    ```
    # 成员检测检测得是key内容
    d = {"one":1, "two":2, "three":3}
    if 2 in d:
        print("value")
    if "two" in d:
        print("key")
    if("two",2) ind d:
        print("kv")
    # 输出结果：
        key
    ```
- 4.字典生成式
    ```
    d = {"one":1, "two":2, "three":3}
    # 常规字典生成式
    dd = {k:v for k,v in d.items()}
    print(dd)
    
    # 加限制条件的字典生成式
    dd = {k:v for k,v in d.items() if v%2==0}
    print(dd)
    ```
## 4.4 字典相关函数
- 1.通用函数：len, max, min, dict
- 2.str(字典)：返回字典的字符串格式
    ```
    d = {"one":1, "two":1, "three":3}
    print(str(d))
    ```
- 3.clear
- 4.items:返回字典的键值对组成的元组格式
    ```
    d = {"one":1, "two":2, "two":3}
    i = d.items()
    print(type(i))
    print(i)
    ```
    ```
    # keys:返回字典的键组成的一个结构
    k = d.keys()
    print(type(k))
    print(k)
    ```
    ```
    # values: 同理，一个可迭代的结构
    v = d.values()
    print(type(v))
    print(v)
    ```
- 5.get:根据指定键返回对应的值，好处是，可以设置默认值
    ```
    d = {"one":1, "two":2, "two":3}
    print(d.get("on333")   # 输出：None
    # get 默认值是None，可以设置
    print(d.get("one", 100)
    print(d.get("one111", 100))
    
    # 体会以下代码跟上面代码的区别
    print(d['one111'])
    ```
- 6.fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有的键的值
    ```
    l = ["enis", "zwei", "dree"]
    # 注意fromkyes两个参数的类型
    # 注意fromkeys的调用主体
    d = dict.fromkeys(l, "hahahahaha")
    print(d)
    ```