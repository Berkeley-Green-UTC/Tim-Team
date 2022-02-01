import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
with open('log.txt', 'a') as f:
  print("Computer IP Address is:" + IP_addres)
