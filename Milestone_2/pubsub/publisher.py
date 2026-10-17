# Author: Thomas Johnson, Koji Maniago
# Date: 2026/10/13

# Publisher
# E-Commerce

import socket
import marshal
print("Server is up, waiting for connections...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 5003))
sock.listen(3)
subscribers = []

# Has to be done through marshalling/unmarshalling

# Broadcast

message = b"Welcome to the E-Commerce Publisher Service!\n"
message += b"=" * 50

message += b"\nUpdates on products, promotions, and analytical news:"
message += b"\nNotifications: Shirts, Pants, and Shoes are back In-Stock!"
#message += b"\nPromotions: Buy 1 Get 1 Free!"
#message += b"\nAnalytics: Here are the latest sales data for this month."
bytes = marshal.dumps(message)
redata = marshal.loads(bytes)
# Accepted Connections: 3
for i in range(3):
    conn, addr = sock.accept()
    subscribers.append(conn)
    print("Connected to:", addr)

for conn in subscribers:
    conn.sendall(redata)


