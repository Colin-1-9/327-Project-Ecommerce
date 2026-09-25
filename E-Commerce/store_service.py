import socket
def store_server():
  customer_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  customer_sock.bind(("127.0.0.1", 5002))
  inventory_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  while True:
    data, addr = customer_sock.recvfrom(1024)
    item = data.decode()[12]
    if item == 's':
      product_name = data.decode()[25:]
      inventory_sock.sendto(item.encode(), ("127.0.0.1", 5003))
      response, _ = inventory_sock.recvfrom(1024)
      customer_sock.sendto(response, addr)