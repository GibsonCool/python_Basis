from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

# 接受来自连接的欢迎语
print(s.recv(1024).decode('utf-8'))
while True:
    inputStr = input("请输入..:")
    s.send(inputStr.encode('utf-8'))
    if inputStr == 'exit':
        break
print("客户端退出")