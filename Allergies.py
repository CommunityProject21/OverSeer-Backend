import pandas as pd

pd.options.mode.chained_assignment = None


def importData():
    patient_allergies_path = "./static/DataSets/Details/allergies.csv"
    allergies = pd.read_csv(patient_allergies_path)
    return allergies


def returnData(patient_id):
    # global patient_allergies
    patient_allergies = importData()
    index = 0
    data = {}
    found = 0
    for i in patient_allergies["PATIENT"]:
        if patient_id == i:
            data['Allergy' + str(len(data)+1)] = str(patient_allergies["DESCRIPTION"][index])
            found = 1
        index = index + 1

    if found == 0:
        return {"message": "No Allergies to Report for given ID."}
    else:
        data["message"] = "Take care of these while interacting with Patient"
        return data
