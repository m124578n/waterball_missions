import time
import sys


class MagicDel:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("刪除中")


p = MagicDel("John")
print(sys.getrefcount(p))  # +1
p1 = p
print(sys.getrefcount(p))
del p1
print(sys.getrefcount(p))
time.sleep(2)
print("等待兩秒鐘")
