import pandas as pd

pd.options.mode.chained_assignment = None


def importData():
    patient_allergies_path = "./static/DataSets/Details/allergies.csv"
    allergies = pd.read_csv(patient_allergies_path)
    return allergies


def returnData(patient_id):
    # global patient_allergies
    patient_allergies = importData()
    patient_allergies["STOP"] = patient_allergies["STOP"].apply(str)
    index = 0
    data = {}
    data["allergies"]=[]
    found = False
    for i in patient_allergies["PATIENT"]:
        if patient_id == i:
            record={}
            record['allergy']=str(patient_allergies["DESCRIPTION"][index])
            record['start']=patient_allergies["START"][index]
            if(patient_allergies["STOP"][index]!="nan"):
                record['stop']=patient_allergies["STOP"][index]
            else:
                record['stop']="Still have the allergy"
            data['allergies'].append(record)
            found = True
        index = index + 1

    if found:
        data["message"] = "Take care of these while interacting with Patient"
        return data
    else:
        return {"message": "No allergies to Report for given ID."}
        
