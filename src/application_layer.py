class ApplicationLayer:
    def __init__(self):
        pass

    def send(self, data):
        """
        The send method is responsible for sending data to the other system.
        """
        # check if data is a string
        if not isinstance(data, str):
            raise TypeError("Data must be a string")
        print(f"Sending data: {data}")

    def receive(self, data):
        """
        The receive method is responsible for receiving data from the other system.
        """
        
        # Validate the data
        if not isinstance(data, bytes):
            raise TypeError("Data must be a byte string")
        data = data.decode('utf-8')
        print(f"Received data: {data}")
