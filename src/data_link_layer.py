class DataLinkLayer:
    def __init__(self):
        pass

    def frame(self, data):
        """
        The frame method is responsible for framing data into blocks or frames.
        """
        # Convert data from bytes to string
        data = data.decode('utf-8')
        # Add a start and end delimiter to the data
        frame = "start" + data + "end"
        return frame

    def unframe(self, frame):
        """
        The unframe method is responsible for unframing blocks or frames into data.
        """
        # Remove the start and end delimiter from the frame
        data = frame.replace("start", "").replace("end", "")
        return data