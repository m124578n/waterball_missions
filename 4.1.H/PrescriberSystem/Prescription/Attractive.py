from .Prescription import Prescription


class Attractive(Prescription):
    def __init__(self):
        self.name: str = "青春抑制劑"
        self.potential_disease: str = "有人想你了 (專業學名：Attractive)"
        self.medicines: list[str] = ["假鬢角", "臭味"]
        self.usage: str = "把假鬢角黏在臉的兩側，讓自己異性緣差一點，自然就不會有人想妳了。"

    def __repr__(self):
        return f"""
        處方名字：{self.name}
        潛在疾病：{self.potential_disease}
        食用藥物：{self.medicines}
        使用方法：{self.usage}
        """
