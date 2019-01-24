"""
    多线程服务器
"""
from socket import *
from threading import Thread
from time import sleep

utf8 = 'utf-8'


# 处理客服端的请求并执行
def tcplink(newSocket, destAddr):
    print(" Accept new  connection from %s:%s" % destAddr)
    newSocket.send(b'Welcome ..')
    while True:
        recvData = newSocket.recv(1024)
        sleep(1)
        if not recvData or recvData.decode(utf8) == 'exit':
            break
        print(recvData.decode(utf8))
    newSocket.close()
    print("Connection from %s:%s is finished!" % destAddr)


def main():
    serScoket = socket(AF_INET, SOCK_STREAM)
    serScoket.bind(('127.0.0.1', 9999))
    serScoket.listen(5)
    print("Waiting for connection.....")
    while True:
        # 接受一个新连接:
        sock, addr = serScoket.accept()
        # 通过创建一个新线程来处理TCP连接
        client_thread = Thread(target=tcplink, args=(sock, addr))
        client_thread.start()


if __name__ == '__main__':
    main()
