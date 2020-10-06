from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("www.google.org",80)) # Connect
s.send("GET /index.html HTTP/1.0\n\n") # Send request
data = s.recv(10000) # Get response
s.close()
