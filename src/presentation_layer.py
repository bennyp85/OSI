class PresentationLayer:
    def __init__(self):
        pass

    def encode(self, data):
        """
        The encode method is responsible for encoding data into a form that can be transmitted over the network.
        """
        # For simplicity, let's assume we're just converting the data to a byte string
        encoded_data = data.encode('utf-8')
        return encoded_data

    def decode(self, data):
        """
        The decode method is responsible for decoding data back into its original form.
        """
        # For simplicity, let's assume we're just converting a byte string back to a string
        decoded_data = data.encode('utf-8')
        return decoded_data