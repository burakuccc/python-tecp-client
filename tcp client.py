from socket import *
host = input("Please enter the host: ")
port = input("Please enter the port")
s = socket(AF_INET,SOCK_STREAM)
s.connect((host,port))
s.sendall("GET /index.html HTTP/1.0\n\n".encode())
data = s.recv(10000)
print(data)
print(len(data))

s.close
