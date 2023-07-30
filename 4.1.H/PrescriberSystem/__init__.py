from .PatientDatabase import PatientDatabase
from .Prescriber import Prescriber
from .PrescriptionHandler import (
    SleepApneaSyndromeHandler,
    COVID_19Handler,
    AttractiveHandler,
    HandlerChain
)

import json
import threading


handler_dict = {
            "COVID-19": COVID_19Handler(),
            "Attractive": AttractiveHandler(),
            "SleepApneaSyndrome": SleepApneaSyndromeHandler()
        }


class PrescriberSystem:
    def __init__(self, save_type, json_name, txt_name):
        self.handler_chain = None
        self.prescriber = None
        self.database = None
        self.doing = True
        self.save_type = save_type
        self.patients = []
        self._read_file(
            json_name=json_name,
            txt_name=txt_name
            )
    
    def prescribe(self):
        a = threading.Thread(target=self._input_patient)
        b = threading.Thread(target=self._prescribe)
        a.start()
        b.start()

    def _input_patient(self):
        while self.doing:
            id_number = input('請輸入病人身份證號碼：')
            symptoms = input("請輸入症狀：")
            symptoms = symptoms.split(", ")
            self.patients.append((id_number, symptoms))
            # self.prescriber.prescribe(id_number, symptoms)
            # choose = input("繼續看診嗎？ yes/no：")
            # if choose == 'no':
            #     self.doing = False
    
    def _prescribe(self):
        while True:
            if self.patients:
                patient = self.patients.pop(0)
                id_number = patient[0]
                symptoms = patient[1]
                prescription = self.prescriber.prescribe(id_number, symptoms)
                self.database.add_case_with_id(id_number, prescription)
                # self._report_data()

    def _report_data(self):
        with open('data.json', 'w') as f:
            if self.save_type == 'json':
                json.dump(self.database.patients, f)

    def _read_file(self, json_name, txt_name):
        self.database = PatientDatabase(json_name)
        self._deal_with_txt(txt_name)
        self.prescriber = Prescriber(self.handler_chain, self.database)

    def _deal_with_txt(self, txt):
        with open(txt, 'r') as f:
            txt_datas = f.read()
        self._get_txt_datas(txt_datas)

    def _get_txt_datas(self, txt_datas):
        """
        if you want to add new prescription,
        you should add here, too.
        """
        datas = txt_datas.split('\n')
        
        handler_chain = HandlerChain()
        for data in datas:
            handler_chain.set_next(handler_dict[data])
        self.handler_chain = handler_chain
