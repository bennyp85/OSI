import hashlib

class NetworkLayer:
    def __init__(self):
        self.routes = {}  # A dictionary to store routes

    def add_route(self, destination, next_hop):
        """
        Add a route to the routing table.
        """
        #encrypt and hash the destination before adding it to the routing table
        print(f"Adding route to {destination} via {next_hop}")
        destination = destination.encode('utf-8')
        destination = hashlib.sha256(destination).hexdigest()
        print(f"Encrypted destination: {destination}")
        
        self.routes[destination] = next_hop

    def route(self, destination):
        """
        Determine the next hop for a packet with the given destination.
        """
        return self.routes.get(destination, None)

    def forward(self, packet):
        """
        Forward a packet along the appropriate route.
        """
        destination = packet.destination

        #decrypt the destination before forwarding the packet
        destination = destination.decode('utf-8')
        destination = hashlib.sha256(destination).hexdigest()
        next_hop = self.route(destination)
        if next_hop is None:
            print(f"No route to {destination}")
        else:
            print(f"Forwarding packet to {next_hop}")
