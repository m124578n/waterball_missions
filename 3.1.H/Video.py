

class Video:
    def __init__(self, title, description, length):
        self.title = title
        self.description = description
        self.length = length
        self.channel = None

    def set_channel(self, channel):
        self.channel = channel
