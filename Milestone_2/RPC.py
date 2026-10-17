import socket
import json
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s")

if len(sys.argv) > 1 and sys.argv[1] == "client":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 5004))
    request = {"method": "get_products"}
    print("Before marshalling:", request)
    sock.sendall(json.dumps(request).encode())
    data = sock.recv(4096)
    print("After unmarshalling:", json.loads(data.decode()))
    sock.close()
else:
    print("RPC server is up, waiting for a request...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5004))
    server.listen(3)
