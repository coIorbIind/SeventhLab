class ProcessData:
    def __init__(self, email, message):
        self.email = email
        self.msg = message

    def __str__(self):
        return f"Email: {self.email}.\nMSG: {self.msg}."
