import json

from .Patient import Patient


class PatientDatabase:
    def __init__(self, file_name: str):
        self.patients: list[Patient] = []
        self.get_datas_by_file(file_name)

    def get_patient_by_id(self, id_number):
        for patient in self.patients:
            if patient.id == id_number:
                return patient

    def get_datas_by_file(self, file_name):
        with open(file_name, 'r') as f:
            file_data = f.read()
        self.deal_with_datas_to_objects(file_data)

    def deal_with_datas_to_objects(self, file_data):
        datas = json.loads(file_data)
        for data in datas:
            patient = Patient(
                datas[data].get('id'),
                datas[data].get('name'),
                datas[data].get('gender'),
                datas[data].get('age'),
                datas[data].get('height'),
                datas[data].get('weight')
            )
            self.patients.append(patient)

    def add_case_with_id(self, id_number, case):
        patient = self.get_patient_by_id(id_number)
        if patient.cases is None:
            patient.cases = [case]
        else:
            patient.cases.append(case)


# p = PatientDatabase('/Users/john/PythonGroup/PythonGroup/4.1.H/Patient.json')
# p.add_case_with_id('A123456789', 'test_case')
# print(p.patients)
