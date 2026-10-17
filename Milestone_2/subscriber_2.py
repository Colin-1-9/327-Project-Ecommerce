# Author: Thomas Johnson
# Date: 2026/10/13

# Subscriber : Marketing Service
# E-Commerce

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5003))

data = client.recv(1024)
print(data.decode())
