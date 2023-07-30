from .PrescriptionHandler import PrescriptionHandler
from ..Prescription import COVID_19
from ..Case import Case
from datetime import datetime


class COVID_19Handler(PrescriptionHandler):
    def __init__(self):
        super().__init__()

    def prescribe(self, patient, symptoms):
        if 'Headache' in symptoms and 'Cough' in symptoms:
            case = Case(
                symptom=symptoms,
                prescription=COVID_19(),
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


