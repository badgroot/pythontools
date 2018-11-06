#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 50000                # Reserve a port for your service.

print ('Server started!')
print ('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
while True:
   msg = c.recv(1024)
   print (addr, ' >> ', msg )
   msg = str(input('SERVER >> '))
   c.send(msg.encode());
   #c.close()                # Close the connection
