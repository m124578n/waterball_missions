

class MagicFormat:
    def __init__(self, name):
        self.name = name

    def __format__(self, format_spec):
        return f"我的名字是：{self.name}"


f = MagicFormat("John")
print(f"My name is :{f.name}")
print(format(f))
print(f"{f}")
print("%s" % f)

# output
# My name is :John
# 我的名字是：John
# 我的名字是：John
# <__main__.MagicFormat object at 0x100a79fd0>


data_dict = {
    'ymd': '{0.year}:{0.month}:{0.day}',
    'dmy': '{0.day}/{0.month}/{0.year}',
    'mdy': '{0.month}-{0.day}-{0.year}'
}


class MyText:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        fmt = data_dict[format_spec]
        return fmt.format(self)


d1 = MyText(2019, 9, 17)
print('{:ymd}'.format(d1))
print('{:dmy}'.format(d1))
print('{:mdy}'.format(d1))

# output
# 2019:9:17
# 17/9/2019
# 9-17-2019
