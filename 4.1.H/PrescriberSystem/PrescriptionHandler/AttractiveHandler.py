from .PrescriptionHandler import PrescriptionHandler
from ..Prescription import Attractive
from ..Case import Case
from datetime import datetime


class AttractiveHandler(PrescriptionHandler):
    def __init__(self):
        super().__init__()

    def prescribe(self, patient, symptoms):
        if patient.age == 18 and 'Sneeze' in symptoms:
            case = Case(
                symptom=symptoms,
                prescription=Attractive(),
                case_time=datetime.now()
            )
            # print(case.prescription)
            return case
        else:
            if self.next is None:
                # print("無符合的處方箋")
                return None
            else:
                return self.next.prescribe(patient, symptoms)
