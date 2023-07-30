

class Channel:
    def __init__(self, name):
        self.name = name
        self.videos = []
        self.subscribers = []

    def notify(self, video):
        for subscriber in self.subscribers:
            subscriber.get_notify(video)

    def upload(self, video):
        self.videos.append(video)
        video.set_channel(self)
        print(f'頻道 {self.name} 上架了一則新影片 "{video.title}"。')
        self.notify(video)
