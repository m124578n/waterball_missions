from .Prescription import Prescription


class SleepApneaSyndrome(Prescription):
    def __init__(self):
        self.name: str = "打呼抑制劑"
        self.potential_disease: str = "睡眠呼吸中止症（專業學名：SleepApneaSyndrome）"
        self.medicines: list[str] = ["一捲膠帶"]
        self.usage: str = "睡覺時，撕下兩塊膠帶，將兩塊膠帶交錯黏在關閉的嘴巴上，就不會打呼了。"

    def __repr__(self):
        return f"""
        處方名字：{self.name}
        潛在疾病：{self.potential_disease}
        食用藥物：{self.medicines}
        使用方法：{self.usage}
        """
