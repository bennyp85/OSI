class DataLinkLayer:
    def __init__(self):
        pass

    def frame(self, data):
        """
        The frame method is responsible for framing data into blocks or frames.
        """
        # check if data is a byte string
        if not isinstance(data, bytes):
            raise TypeError("Data must be a byte string")
        # Convert data from bytes to string
        data = data.decode('utf-8')
        # Add a start and end delimiter to the data
        frame = "start" + data + "end"
        return frame

    def unframe(self, frame):
        """
        The unframe method is responsible for unframing blocks or frames into data.
        """
        # check if frame is a string
        if not isinstance(frame, str):
            raise TypeError("Frame must be a string")
        # Remove the start and end delimiter from the frame
        data = frame.replace("start", "").replace("end", "")
        return data