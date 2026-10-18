
import socket
import json
import sys

# Get the port number from the terminal
port = int(sys.argv[1])

# Create a UDP socket
receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Listen for messages on this port
receiver.bind(("127.0.0.1", port))

print(f"Node listening on port {port}...")
print("Waiting for group message...")

# Receive the message
data, address = receiver.recvfrom(4096)

# Convert JSON bytes back into a Python dictionary
message = json.loads(data.decode("utf-8"))

with open('messagelogging.txt', 'a') as f:
        f.write(f"\nPort {port} received message from {address}, {message['sender']}\nEvent: {message['event']}\nProduct: {message['product']}\nStatus: {message['status']}\nTimestamp: {message['timestamp']}\n")
print(f"Message received from {address}")
print(f"Sender: {message['sender']}")
print(f"Event: {message['event']}")
print(f"Product: {message['product']}")
print(f"Status: {message['status']}")
print(f"Timestamp: {message['timestamp']}")

receiver.close()
