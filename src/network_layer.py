class NetworkLayer:
    def __init__(self):
        self.routes = {}  # A dictionary to store routes

    def add_route(self, destination, next_hop):
        """
        Add a route to the routing table.
        """
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
        next_hop = self.route(destination)
        if next_hop is None:
            print(f"No route to {destination}")
        else:
            print(f"Forwarding packet to {next_hop}")