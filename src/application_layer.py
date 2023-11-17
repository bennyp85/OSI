class ApplicationLayer:
    def __init__(self):
        pass

    def send(self, data):
        """
        The send method is responsible for sending data to the other system.
        """
        # For simplicity, let's just print the data
        print(f"Sending data: {data}")

    def receive(self, data):
        """
        The receive method is responsible for receiving data from the other system.
        """
        
        # Decode the byte string
        data = data.decode('utf-8')
        print(f"Received data: {data}")
