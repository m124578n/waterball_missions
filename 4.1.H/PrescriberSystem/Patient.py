from dataclasses import dataclass, field
from .Case import Case


@dataclass
class Patient:
    id: str
    name: str
    gender: str
    age: int
    height: float
    weight: float
    cases: list[Case] = None

    def __post_init__(self):
        self.BMI = round(self.weight / ((self.height/100)**2), 1)

