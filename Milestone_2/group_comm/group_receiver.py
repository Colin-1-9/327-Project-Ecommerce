
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

print(f"\nMessage received from {address}")
print(f"Sender: {message['sender']}")
print(f"Event: {message['event']}")
print(f"Product: {message['product']}")
print(f"Status: {message['status']}")
print(f"Timestamp: {message['timestamp']}")

receiver.close()
