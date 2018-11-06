import socket
import sys

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Successfully created")
except:
    print("socket creation failed %s",err)

port=80

try:
    host_ip=socket.gethostbyname('www.google.com')

except socket.gaierror:
    print ("there was an error resolving host")
    sys.exit()

s.connect((host_ip,port))
print("the socket has successfully connected to google on port ==%s" ,(host_ip))
