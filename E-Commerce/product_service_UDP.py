#product server
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5002))

stock = {"steak": 8, "chicken": 10, "fish": 5, "rice": 12, "beans": 12}

while True:
    data, addr = sock.recvfrom(1024)
    items = data.decode()
    if items in stock:
        response = f"{items} is in stock: {stock[items]} available"
    else:
        response= f"{items} is not in stock"
    sock.sendto(response.encode(),addr)
