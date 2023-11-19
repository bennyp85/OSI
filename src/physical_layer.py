class PhysicalLayer:
    """
    The PhysicalLayer class represents the physical layer of the OSI model.
    It is responsible for the transmission and reception of raw bitstreams over a physical medium.
    """
    def __init__(self):
        pass

    def transmit(self, data):

        bitstream = self.data_to_bitstream(data)
        # Code to transmit bitstream goes here
        # check to see if the data is a bitstream
        if not isinstance(bitstream, str):
            raise TypeError("Data must be a bitstream")
        return bitstream

    def receive(self, received_bitstream):
        # Code to receive bitstream goes here
        data = self.bitstream_to_data(received_bitstream)
        return data

    def data_to_bitstream(self, data):
        bitstream = ""
        for character in data:
            bitstream += bin(ord(character))[2:].zfill(8)
        return bitstream

    def bitstream_to_data(self, bitstream):
        data = ""
        for i in range(0, len(bitstream), 8):
            data += chr(int(bitstream[i:i+8], 2))
        return data

