from abc import ABC, abstractmethod


class YoutubeUser(ABC):
    def __init__(self, name):
        self.name = name
        self.subscribed_channel = []

    def subscribe(self, *Channels):
        for channel in Channels:
            self.subscribed_channel.append(channel)
            channel.subscribers.append(self)
            print(f"{self.name} 訂閱了 {channel.name}")

    def unsubscribe(self, *Channels):
        for channel in Channels:
            self.subscribed_channel.remove(channel)
            channel.subscribers.remove(self)
            print(f"{self.name} 解除訂閱了 {channel.name}")

    @abstractmethod
    def get_notify(self, video):
        pass

