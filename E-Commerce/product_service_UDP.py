#product server
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5002))

products = []

while True:
    data, addr = sock.recvfrom(1024)
    user_role = data.decode()[12]
    if user_role == 's':
        product_name = data.decode()[25:]
        products.append(product_name)
        sock.sendto(b"added "+products[-1].encode()+b" to product database\n" + 
                b"ack: " +data, addr)
    else:
        sock.sendto(b"ack: " +data, addr)