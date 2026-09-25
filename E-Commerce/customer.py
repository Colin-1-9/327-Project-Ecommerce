import socket
import time

def customer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b"ack: ",("127.0.0.1", 5002))
    data, _ = sock.recvfrom(1024)
    print("Received: ",data.decode())
    time.sleep(1)