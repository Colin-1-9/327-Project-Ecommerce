# user client
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

seller = False
if input("Are you a seller? (y/n)\n") == ('y'):
    seller = True

if seller:
    product = input("\ninput product name\n")
    sock.sendto(b"hello from seller via udp "+product.encode(), ("127.0.0.1", 5002))
else:
    sock.sendto(b"hello from customer via udp", ("127.0.0.1", 5002))
data, _ = sock.recvfrom(1024)
print(data.decode())

if input("Place order? (y/n)") == 'y':
    sock.sendto(b"sendproducts", ("127.0.0.1", 5002))
    data, _ = sock.recvfrom(1024)
    print(data.decode())
    product_purchased = input("choose item to purchase\n")
    print("contacting order service")
    sock.sendto(b"orderplaced", ("127.0.0.1", 5003))