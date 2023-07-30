from YoutubeUser import YoutubeUser


class WaterBall(YoutubeUser):
    def get_notify(self, video):
        if video.length >= 180:
            print(f'{self.name} 對影片 "{video.title}" 按讚。')
