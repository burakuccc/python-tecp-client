from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect(('www.python.org',80))
s.sendall("GET /index.html HTTP/1.0\n\n".encode())
data = s.recv(10000)
print(data)
print(len(data))

s.close
