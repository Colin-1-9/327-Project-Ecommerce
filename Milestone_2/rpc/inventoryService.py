import socket

products = ["Shirts", "Pants", "Shoes"]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5003))
server.listen(3)

print("Inventory service is running, waiting for requests...")

while True:
    conn, addr = server.accept()
    with conn:
        request = conn.recv(1024)

        if request == b"getproducts":
            conn.sendall(b'Shirts, Pants, Shoes')
