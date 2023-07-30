import time

from .PatientDatabase import PatientDatabase


class Prescriber:
    def __init__(self, handler, database):
        self.handler = handler.handler
        self.database: PatientDatabase = database

    def prescribe(self, id_number, symptoms):
        patient = self.database.get_patient_by_id(id_number)
        time.sleep(3)
        prescription = self.handler.prescribe(patient, symptoms)
        return prescription


# p = Prescriber('/Users/john/PythonGroup/PythonGroup/4.1.H/Prescription.txt')
