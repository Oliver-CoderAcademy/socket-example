class Message():
    def __init__(self, text: str):
        self.text="<"+text+">"
        self.text=self.text.strip("b'")
        self.text=self.text[0:1024]

    def __repr__(self) -> str:
        return self.text

    def send(self):
        pass