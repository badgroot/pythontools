import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 9760                
  
# connect to the server on local computer 
s.connect(('192.168.100.115', port)) 
s.send(100) 
# receive data from the server 
print ("%s",s.recv(1024)) 
# close the connection 
s.close()       
