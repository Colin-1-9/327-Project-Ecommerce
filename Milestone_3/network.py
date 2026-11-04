from peer import Peer

def main():
    # Create peers
    peer_1 = Peer(1, ["Clothing"])
    peer_2 = Peer(2, ["Shoes"])
    peer_3 = Peer(3, ["Supplies"])
    peer_4 = Peer(4, ["Backpacks"])
    peer_5 = Peer(5, ["Books"])

    peer_1.neighbors = [peer_2, peer_3]
    peer_2.neighbors = [peer_1, peer_4]
    peer_3.neighbors = [peer_1, peer_4]
    peer_4.neighbors = [peer_2, peer_3]

    # Peer 5 joins the network by connecting to peer 1
    peer_5.join(peer_1)

    # Peer 3 leaves the network by disconnecting from peer 1
    peer_3.leave(peer_1)

    # Peer 1 looks up a product in the network
    print("\nLooking up product: Backpacks:")
    lookup_products = "Backpacks"
    peer_id = peer_1.lookup(lookup_products)
    
    if peer_id:
        print(f"\nProduct '{lookup_products}' found at Peer {peer_id}.")
    else:
        print(f"Product '{lookup_products}' not found in the network.")

if __name__ == "__main__":
    main()
