from .Prescription import Prescription


class COVID_19(Prescription):
    def __init__(self):
        self.name: str = "清冠一號"
        self.potential_disease: str = "新冠肺炎（專業學名：COVID-19）"
        self.medicines: list[str] = ["清冠一號"]
        self.usage: str = "將相關藥材裝入茶包裡，使用500 mL 溫、熱水沖泡悶煮1~3 分鐘後即可飲用。"

    def __repr__(self):
        return f"""
        處方名字：{self.name}
        潛在疾病：{self.potential_disease}
        食用藥物：{self.medicines}
        使用方法：{self.usage}
        """
