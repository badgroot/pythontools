
# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys
import datetime
import time
today = datetime.date.today()
DateTime=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
print(DateTime)
sendData="Tachyon Led solutions"
host_addr='192.168.100.2'
port_num=9760
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s",(err)) 
  
# default port for socket 
port = 9760
  
try: 
    host_ip = '192.168.100.3' 
except socket.gaierror: 
  
    # this means could not resolve the host 
    print ("there was an error resolving the host %s",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    sys.exit() 
  
# connecting to the server 
languages = [64,65,65]
n=100000
counter = 1
counter2=0
while counter2 <= n:
    counter += 1
    #counter2=counter2+1
    DateTime=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    print(DateTime)
    print("Packet number is %d",counter)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
            print ("socket creation failed with error %s",(err))
            # default port for socket
            port = port_num
            try:
                host_ip = host_addr
            except socket.gaierror:
                # this means could not resolve the host
                print ("there was an error resolving the host %s",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
                sys.exit() 
    try:
        s.connect((host_ip, port))
        getdata=s.recv(1024)
        print ("data recieved from server %s",(getdata))
        s.send(sendData.encode())
        s.send(DateTime.encode())
        s.send("Packet NUmber".encode())
        s.send(bytes(counter))
        #s.send(bytes(languages));
        print ("the socket has successfully connected to google on port == %s",(host_ip))
        s.close()
        time.sleep(1)
    except socket.gaierror:
        print("server is down on host_ip=%s,port=%d %s",host_ip,port,(err))
    

