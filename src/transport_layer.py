class TransportLayer:
    def __init__(self):
        pass

    def segment(self, data, segment_size):
        """
        The segment method is responsible for segmenting data into smaller pieces.
        """
        # check it data is a byte string
        if not isinstance(data, bytes):
            raise TypeError("Data must be a string")
        segments = [data[i:i+segment_size] for i in range(0, len(data), segment_size)]
        return segments

    def reassemble(self, segments):
        """
        The reassemble method is responsible for reassembling segmented data back into its original form.
        """
        # check if segments is a list
        if not isinstance(segments, list):
            raise TypeError("Segments must be a list")
        data = "".join(segments)
        return data