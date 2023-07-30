from YoutubeUser import YoutubeUser


class FireBall(YoutubeUser):
    def get_notify(self, video):
        if video.length <= 60:
            self.unsubscribe(video.channel)
