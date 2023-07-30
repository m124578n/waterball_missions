from dataclasses import dataclass
from datetime import datetime

from .Prescription import Prescription


@dataclass
class Case:
    symptom: list[str]
    prescription: Prescription
    case_time: datetime
