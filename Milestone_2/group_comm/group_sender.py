
import socket
import json
from datetime import datetime

# Three receiving nodes on the same computer
nodes = [
    ("127.0.0.1", 6001),
    ("127.0.0.1", 6002),
    ("127.0.0.1", 6003)
]

# Create a UDP socket
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create a group message
message = {
    "sender": "Inventory Service",
    "event": "Inventory Update",
    "product": "Shirts",
    "status": "Back in stock",
    "timestamp": datetime.now().isoformat()
}

# Convert the message into JSON bytes
data = json.dumps(message).encode("utf-8")

# Send the same message to all three nodes
for address in nodes:
    sender.sendto(data, address)
    print(f"Message sent to {address}")

sender.close()
print("Group message sent to all nodes.")
