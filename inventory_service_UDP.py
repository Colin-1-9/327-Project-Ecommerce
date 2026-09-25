#inventory service
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5003))

products = {"cell phone": 5, "book": 3, "toy food": 8}

while True:
    data, addr = sock.recvfrom(1024)
    if data.decode() == "getproducts":
        product_list = ", ".join(list(products.keys())).encode()
        sock.sendto(product_list, addr)

    elif data.decode() == "orderplaced":
        print("order recieved")
        sock.sendto(b"order received", addr)

    else:
        sock.sendto(b"ack: " + data, addr)