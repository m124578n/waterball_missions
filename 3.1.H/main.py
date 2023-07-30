from Channel import Channel
from WaterBall import WaterBall
from FireBall import FireBall
from Video import Video


if __name__ == '__main__':
    pewdiepie = Channel('PewDiePie')
    wsa = Channel('水球軟體學院')
    水球 = WaterBall('水球')
    火球 = FireBall('火球')
    水球.subscribe(pewdiepie, wsa)
    火球.subscribe(pewdiepie, wsa)
    wsa.upload(Video('C1M1S2', '這個世界正式物件導向的呢！', 240))
    pewdiepie.upload(Video('Hello guys', 'Clickbait', 30))
    wsa.upload(Video('C1M1S3', '物件 vs. 類別！', 60))
    pewdiepie.upload(Video('Minecraft', "Let's play Minecraft", 1800))

