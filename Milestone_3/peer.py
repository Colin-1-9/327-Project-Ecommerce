class Peer:
    def __init__(self, peer_id, products):
        self.id = peer_id
        self.neighbors = []
        self.products = products

    def join(self, peer):
        print(f"Peer {self.id} is joining the network through Peer {peer.id}")
        self.neighbors.append(peer)
        print(f"Peer {self.id} has joined the network.")

    def leave(self, peer):
        print(f"\nPeer {self.id} is leaving the network through Peer {peer.id}")
        self.neighbors.remove(peer)
        print(f"Peer {self.id} has left the network.")

    def lookup(self, product, visited = None):
        if visited is None:
            visited = set()

        visited.add(self.id)

        print(f"Peer {self.id} checking for {product}")

        if product in self.products:
            return self.id
        
        for neighbor in self.neighbors:
            if neighbor.id not in visited:
                result = neighbor.lookup(product, visited)

                if result:
                    return result 
            
        return None
