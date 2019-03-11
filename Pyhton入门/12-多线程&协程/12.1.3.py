'''
利用time函数，生成两个函数
利用多线程调用
计算总运行时间
练习带参数的多线程启动方法
'''
import time
# 导入多线程并更名为thread
import _thread as thread

def loop1(in1):
    # ctime 得到当前时间
    print("Start loop 1 at:", time.ctime())
    # 把参数打印出来
    print("我是参数 ", in1)
    # 睡眠时间，单位是秒
    time.sleep(4)
    print("End loop1 at:", time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print("Start loop 2 at:", time.ctime())
    # 把参数in1 和 in2打印出来，代表使用
    print("我是参数 ", in1, "和参数 ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at:", time.ctime())

def main():
    print("主程序开始于：", time.ctime())

    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个，一个是需要运行的函数名，一个是函数的参数作为元组使用，为空则使用空元组
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loopl,("tcccc1", ))
    thread.start_new_thread(loop2,("tcccc2","tcccc3"))
    print("主程序结束于：", time.ctime())

if __name__=='__main__':
    main()
    while True:
        time.sleep(1)
