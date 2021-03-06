"""
    相关链接：https://zhuanlan.zhihu.com/p/33325094
    GIL(Global Interpreter Lock)：Python解释器中的一种CPython（目前使用最多的Python解释器，各种Linux和其他OS默认集成的Python都是基于CPython解释器。一些其他的解释器还有：JPython，Pypy）
                                  用来做多线程控制和调度的全局锁。
    GIL的问题：其实是由于近十几年来应用程序和操作系统逐步从多任务单核心演进到多任务多核心导致的 ,
              在一个古老的单核CPU上调度多个线程任务，大家相互共享一个全局锁，谁在CPU执行，谁就占有这把锁，
              直到因为IO或者Timer Tick到期让出CPU，没有在执行的线程就安静的等待着这把锁（除了等待之外，他们应该也无事可做）
    GIL的避免：方法1---》用多进程代替多线程
              方法2---》一些实在需要多线程的地方使用C语言去实现，然后编译成动态库记载使用，直接绕过GIL
"""
