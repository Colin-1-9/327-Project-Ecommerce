
import socket
import json
import sys
import threading

# Peer ID and port from terminal
peer_id = int(sys.argv[1])
port = 6000 + peer_id

# Store connected peers
neighbors = []

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", port))
sock.settimeout(1)

print(f"Peer {peer_id} started on port {port}")

# Listen for messages from other peers
def receive_messages():
    while True:
        try:
            data, address = sock.recvfrom(4096)
            message = json.loads(data.decode())
            sender = message["peer"]

            if message["type"] == "JOIN":
                if sender not in neighbors:
                    neighbors.append(sender)
                print(f"Peer {sender} joined the network")

                reply = {"type": "JOIN_ACK", "peer": peer_id}
                sock.sendto(json.dumps(reply).encode(), address)

            elif message["type"] == "JOIN_ACK":
                if sender not in neighbors:
                    neighbors.append(sender)
                print(f"Connected to Peer {sender}")

            elif message["type"] == "LEAVE":
                if sender in neighbors:
                    neighbors.remove(sender)
                print(f"Peer {sender} left the network")

        except socket.timeout:
            continue
        except OSError:
            break

# Run receiver in background
threading.Thread(target=receive_messages, daemon=True).start()

# Send message to another peer
def send_message(target, event):
    message = {"type": event, "peer": peer_id}
    sock.sendto(json.dumps(message).encode(),
                ("127.0.0.1", 6000 + target))

# User commands
while True:
    command = input("Enter join, leave, or neighbors: ").lower()

    if command == "join":
        target = int(input("Enter peer ID to connect to: "))
        send_message(target, "JOIN")

    elif command == "neighbors":
        print(f"Peer {peer_id} neighbors: {neighbors}")

    elif command == "leave":
        for neighbor in neighbors[:]:
            send_message(neighbor, "LEAVE")
        print(f"Peer {peer_id} leaving the network")
        break

sock.close()
