'''
利用time函数，生成两个函数
利用多线程调用
计算总运行时间
练习带参数的多线程启动方法
'''
import time
# 导入多线程并更名为thread
import _thread as thread
import threading

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
    # 生成 threading.Thread 实例

    t1 = threading.Thread(target=loop1, args=("tc1",))
    t1.start()

    t2 =  threading.Thread(target=loop2, args=("tc2", "tc3"))
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束于：", time.ctime())

if __name__=='__main__':
    main()
    # 这里测试要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主程序执行完毕，则子线程可能也需要终止
    while True:
        time.sleep(1)