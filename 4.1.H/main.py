from PrescriberSystem import PrescriberSystem


if __name__ == '__main__':
    # p = PrescriberSystem(
    #     save_type='json',
    #     json_name="C:/Users/TW000626/Downloads/pythongroup/PythonGroup/4.1.H/Patient.json",
    #     txt_name="C:/Users/TW000626/Downloads/pythongroup/PythonGroup/4.1.H/Prescription.txt"
    #     )
    p = PrescriberSystem(
        save_type='json',
        json_name="/Users/john/PythonGroup/PythonGroup/4.1.H/Patient.json",
        txt_name="/Users/john/PythonGroup/PythonGroup/4.1.H/Prescription.txt"
        )
    p.prescribe()

    # p = PrescriberSystem(
    #     "/Users/john/PythonGroup/PythonGroup/4.1.H/Patient.json",
    #     "/Users/john/PythonGroup/PythonGroup/4.1.H/Prescription.txt"
    # )
    # p.prescriber(id, symptom, format)
    # p.report(result, json or csv)
