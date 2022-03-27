import pandas as pd

pd.options.mode.chained_assignment = None


def importData():
    patient_implants_path = "./static/DataSets/Details/devices.csv"
    implants = pd.read_csv(patient_implants_path)
    return implants


def returnData(patient_id):
    patient_implants = importData()
    index = 0
    data = {}
    data["devices"] = []
    found = False
    for i in patient_implants['PATIENT']:
        if i == patient_id:
            device = {}
            device["name"] = patient_implants['DESCRIPTION'][index]
            device["id"] = patient_implants['UDI'][index]
            data["devices"].append(device)
            found=True
        index = index + 1
    if found:
        return data
    else:
        return {"devices": "No implants for the given User."}
