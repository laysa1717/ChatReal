class Message:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        
class ChatRoom:
    def __init__(self):
        self.messages = []
        
    def add_message(self, message):
        self.messages.append(message)
        
    def get_messages(self):
        return self.messages