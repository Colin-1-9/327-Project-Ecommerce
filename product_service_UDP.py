#product server
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5002))

def update_product_listings():
    sock.sendto(b"getproducts", ("127.0.0.1", 5003))
    data, _ = sock.recvfrom(1024)
    return data.decode().split(", ")


 #create initial product list
products = update_product_listings()
print(products)

while True:

    data, addr = sock.recvfrom(1024)
    #this is for hello and product from seller
    if data.decode().startswith("hello from seller"):
        product_name = data.decode()[25:]
        products.append(product_name)
        sock.sendto(b"added "+products[-1].encode()+b" to product database\n" + 
                b"ack: " +data, addr)

    #for sending product list
    elif data.decode() == "sendproducts":

        product_list = ", ".join(products).encode()
        sock.sendto(product_list, addr)

    #currently just basic customer hello
    else:
        sock.sendto(b"ack: " +data, addr)