import pandas as pd

pd.options.mode.chained_assignment = None


def importData():
    patient_observations_path = "./static/DataSets/Details/observations.csv"
    observations = pd.read_csv(patient_observations_path)
    return observations


def returnData(patient_id):
    patient_observations = importData()
    index = 0
    data = {}
    found = False
    data["observation"]= []
    dates = []
    for i in patient_observations["PATIENT"]:
        if patient_id == i:
            found = True
            dates.append(patient_observations["DATE"][index][:10])
        index=index+1

    # dates.sort()
    for date in sorted(set(dates)):
        data["observation"].append({"date":date,"observations":{}})
    
    index=0
    for i in patient_observations["PATIENT"]:
        if(patient_id == i):
            obj_index=0
            for obj in data["observation"]:
                if(obj.get('date')==patient_observations["DATE"][index][:10]):
                    (data["observation"][obj_index]).get("observations").update({patient_observations["DESCRIPTION"][index]:(str(patient_observations["VALUE"][index])+" "+str(patient_observations["UNITS"][index]))})
                    break
                obj_index=obj_index+1
        index=index+1

    if found:
        return data
    else:
        return {"message": "No Observations found for given ID."}