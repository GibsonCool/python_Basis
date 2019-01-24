"""
    多进程：python的fork()函数，调用一次返回两次。操作系统把当前进程（父进程）复制了一份（子进程）。然后分别在父进程和子进程中返回
           子进程永远返回0，父进程则返回子进程的进程ID。一个父进程可以fork出很多子进程。子进程可以调用getppid()就可以拿到父进程ID
"""
import os

# print('Process (%s) start...' % os.getpid())
# # only work on Unix/Linux/Mac; 在windows上无法运行！垃圾windows
# pid = os.fork()
# if pid == 0:
#     print("I am child process(%s) and my pare nt is %s " % (os.getpid(), os.getppid()))
# else:
#     print("I (%s) just created a child process(%s)" % (os.getpid(), pid))
#
# print("#" * 80)
"""
    python是跨平台的，提供了跨平台的多进程支持模块multiprocessing
"""
from multiprocessing import Process


def run_child_process(name):
    print("Run child process %s (%s)" % (name, os.getpid()))


print("Parent process %s" % os.getpid())
p = Process(target=run_child_process, args=("cxx子进程",))
print("Child process will start.")
p.start()
p.join()  # 等待子进程结束后再继续往下运行
print("Child process end.")

print("#" * 80)

"""
    Pool 进程池，用于批量创建子进程
"""
from multiprocessing import Pool

import time, random


def long_time_task(name):
    print("run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f senconds.." % (name, (end - start)))


p = Pool(4)
for i in range(5):
    p.apply_async(long_time_task, args=(i,))    # 非阻塞方式。任务的执行不会阻塞任务的添加到进程池中
    # p.apply(long_time_task, args=(i,))    # 阻塞方式，等到上一个任务即这里的long_time_task执行完了才能继续添加

print("waiting for all subProcess finish...")
p.close()  # 关闭进程池，光比后P不在接受新的任务或请求
p.join()  # 等待P中的所有子进程执行完成，必须放在close语句之后。
print("All subProcess finished")
print("#" * 80)
