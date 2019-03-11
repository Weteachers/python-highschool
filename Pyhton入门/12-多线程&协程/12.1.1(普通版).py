'''
利用time函数，生成两个函数
顺序调用
计算总运行时间
练习带参数的多线程启动方法
'''
import time

def loopl():
    # ctime 得到当前时间
    print("Start loop 1 at:", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("End loop1 at:", time.ctime())

def loop2():
    # ctime 得到当前时间
    print("Start loop 2 at:", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at:", time.ctime())

def main():
    print("主程序开始于：", time.ctime())
    loopl()
    loop2()
    print("主程序结束于：", time.ctime())

if __name__=='__main__':
    main()