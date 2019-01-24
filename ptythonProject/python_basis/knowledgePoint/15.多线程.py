"""
    多线程：
"""
import threading
import time


def loop():
    print("thread %s is running,,," % threading.current_thread().name)
    n = 0
    while n <= 5:
        n += 1
        print("thread %s -----> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s is ended,,," % threading.current_thread().name)


print("thread %s is running,,," % threading.current_thread().name)
t1 = threading.Thread(target=loop, name="LoopThread")
t1.start()
t1.join()
print("thread %s is ended,,," % threading.current_thread().name)

print("*" * 80)


class MyThread(threading.Thread):
    def run(self):
        for i in range(4):
            time.sleep(1)
            print("thread %s is running ----->value = %d" % (self.name, i))


t2 = MyThread(name="MySelfThread")
t2.start()
t2.join()
print("*" * 80)

"""
    Lock：多线程不同于多进程，线程间的数据是可以共享，共享就存在同时修改容易造成数据紊乱，通过互斥锁来处理
          由于锁只有一个，无论多少线程，同一时刻只能有一个线程持有该锁，所以不会造成修改冲突
"""
sum = 10

# 创建一把互斥锁，
lock = threading.Lock()


def addSum():
    global sum
    # 对操作共享变量的代码块进行上锁，其他线程有需要锁操作的线程就无法操作，一直等待
    lock.acquire()
    for i in range(1000000):
        sum = sum + i
    # 操作共享变量完毕后释放锁，这样其他线程就可以抢到锁释放阻塞，进行执行
    lock.release()


def subSum():
    global sum
    lock.acquire()
    for i in range(1000000):
        sum = sum - i
    lock.release()


t3 = threading.Thread(target=addSum, name="AddThread")
t4 = threading.Thread(target=subSum, name="SubThread")

t3.start()
t4.start()

t3.join()
t4.join()
print("sum=%s" % sum)
