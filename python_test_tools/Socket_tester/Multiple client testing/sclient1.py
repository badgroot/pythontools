import socket
s=socket.socket()
port =8080
s.connect('0.0.0.0',port)
print (s.recv(1024))
s.close()
