import pandas as pd

pd.options.mode.chained_assignment = None


def importData():
    patient_conditions_path = "./static/DataSets/Details/conditions.csv"
    conditions = pd.read_csv(patient_conditions_path)
    return conditions


def returnData(patient_id):
    # global patient_conditions
    patient_conditions = importData()
    patient_conditions["STOP"] = patient_conditions["STOP"].apply(str)
    index = 0
    data = {}
    data["conditions"]=[]
    found = False
    for i in patient_conditions["PATIENT"]:
        if patient_id == i:
            record={}
            record['conditions']=str(patient_conditions["DESCRIPTION"][index])
            record['start']=patient_conditions["START"][index]
            if(patient_conditions["STOP"][index]!="nan"):
                record['stop']=patient_conditions["STOP"][index]
            else:
                record['stop']="Still suffering from this."
            data['conditions'].append(record)
            found = True
        index = index + 1

    if found:
        return data
    else:
        return {"message": "No conditions to Report for given ID."}
        
