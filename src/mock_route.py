    # # Create a mock route
    # mock_route = Mock()
    # mock_route.destination = "192.168.1.1"
    # mock_route.next_hop = "192.168.1.2"
    # network_layer.add_route(mock_route.destination, mock_route.next_hop)

class MockRoute:
    def __init__(self):
        self.destination = ""
        self.next_hop = ""

