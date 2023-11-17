class SessionLayer:
    def __init__(self):
        self.sessions = {}  # A dictionary to store sessions

    def establish(self, session_id):
        """
        The establish method is responsible for establishing a session.
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = "active"
            print(f"Session {session_id} established.")
        else:
            print(f"Session {session_id} already exists.")

    def terminate(self, session_id):
        """
        The terminate method is responsible for terminating a session.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            print(f"Session {session_id} terminated.")
        else:
            print(f"Session {session_id} does not exist.")