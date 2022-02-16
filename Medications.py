import pandas as pd

pd.options.mode.chained_assignment = None


def importData():
    patient_medications_path = "./static/DataSets/Details/medications.csv"
    medications = pd.read_csv(patient_medications_path)
    return medications


def returnData(patient_id):
    patient_medications = importData()
    patient_medications['STOP']= patient_medications['STOP'].apply(str)
    index = 0
    data = {}
    data["medications"] = []
    found = False
    for i in patient_medications['PATIENT']:
        if i == patient_id:
            found=True
            record = {}
            record["name"] = patient_medications['DESCRIPTION'][index]
            if(patient_medications["REASONCODE"][index]>0):
                record["prescription"] = patient_medications['REASONDESCRIPTION'][index]
            else:
                record["prescription"] = ""
            record["start"] = patient_medications["START"][index][:10]+" "+patient_medications["START"][index][11:19]
            if(patient_medications["STOP"][index]!="nan"):
                record["stop"] = patient_medications["STOP"][index][:10]+" "+patient_medications["STOP"][index][11:19]
            else:
                record["stop"] = "Ongoing"
            data["medications"].append(record)
        index = index + 1
    if found:
        return data
    else:
        return {"medcations": "No Medication Records found for the given User."}
