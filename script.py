import socket
IP_address = socket.gethostbyname(h_name)
with open('log.txt', 'a') as f:
  f.write("Computer IP Address is:" + IP_address)
