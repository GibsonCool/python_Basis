"""
    Queue：是multiprocessing模块中，用于实现多进程之间数据传递，本身是一个消息队列程序
           get()
           put()
           empty()
           full()
           qsize()

    Manager().Queue():用于线程池中的通信队列，使用方法与Queue一样

"""

from multiprocessing import Queue, Process, Pool
import time, random


def write(queue):
    for value in ['A', 'B', 'C', 'D']:
        print("Put %s to queue..." % value)
        queue.put(value)
        time.sleep(random.random())


def read(queue):
    while True:
        if not queue.empty():
            value = queue.get(True)
            print("Get %s from queue。。。" % value)
            time.sleep(random.random())

        else:
            break


if __name__ == "__main__":
    q = Queue()  # 不传值表示不限制队列大小

    # 开启两个进程，使用队列进行通信，一个往里面传递消息，一个从里面取消息
    pWrite = Process(target=write, args=(q,))
    pRead = Process(target=read, args=(q,))

    pWrite.start()
    pRead.start()
    pWrite.join()
