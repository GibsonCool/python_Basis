from multiprocessing import Process
import time, os


# 继承Process类
class Process_class(Process):
    """
        因为Process类本身也有__init__方法，之歌子类相当于重写了这个方法，
        为了能完全初始化一个Process类，调用Processs.__init__方法，将这个类自己传入，完成初始化操作
    """

    def __init__(self, interval):
        Process.__init__(self)
        self.__interval = interval

    # 重写Process类的run方法，当调用该实例对象的start时候回触发此方法执行
    def run(self):
        print("子进程(%s) 开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
        t_start = time.time()

        time.sleep(self.__interval)
        t_end = time.time()
        t_spend_time = t_start - t_end
        print("(%s)执行结束，耗时 %0.2f秒" % (os.getpid(), t_spend_time))


if __name__ == "__main__":
    print("当前进程(%s)" % os.getpid())
    p = Process_class(2)
    p.start()
    p.join()
