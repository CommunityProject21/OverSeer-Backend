import pandas as pd
pd.options.mode.chained_assignment = None

def importData():
    patient_details_path = "./static/DataSets/Details/patients.csv"
    details = pd.read_csv(patient_details_path)
    return details


def cleaningData():
    patient_details['PREFIX'] = patient_details['PREFIX'].str.replace('\f+', ' ')
    patient_details['MAIDEN'] = patient_details['MAIDEN'].str.replace('\f+', '')

    index = 0
    for i in patient_details["PREFIX"]:
        if not (isinstance(i, str)):
            patient_details["PREFIX"][index] = ''
        index = index + 1

    index = 0
    for i in patient_details["FIRST"]:
        patient_details["FIRST"][index] = ''.join([i for i in i if not i.isdigit()])
        index = index + 1

    index = 0
    for i in patient_details["LAST"]:
        patient_details["LAST"][index] = ''.join([i for i in i if not i.isdigit()])
        index = index + 1

    index = 0
    for i in patient_details["MAIDEN"]:
        if isinstance(i, str):
            patient_details["MAIDEN"][index] = ''.join([i for i in i if not i.isdigit()])
        else:
            patient_details["MAIDEN"][index] = ''
        index = index + 1

    index = 0
    for i in patient_details["MARITAL"]:
        if i == "M":
            patient_details["MARITAL"][index] = "Married"
        elif i == "S":
            patient_details["MARITAL"][index] = "Single"
        elif i == '':
            patient_details["MARITAL"][index] = "N/A"
        index = index + 1

    index = 0
    for i in patient_details["GENDER"]:
        if i == "M":
            patient_details["GENDER"][index] = "Male"
        if i == "F":
            patient_details["GENDER"][index] = "Female"
        index = index + 1

    return patient_details


def returnData(patient_id):
    global patient_details
    patient_details = importData()
    cleaningData()
    data = {}
    index = -1
    for i in patient_details["Id"]:
        index = index + 1
        if patient_id == i:
            data["name"] = patient_details["PREFIX"][index]+" "+patient_details["FIRST"][index]+" "+patient_details["LAST"][index]
            data["address"] = patient_details["ADDRESS"][index] + ", " + patient_details["CITY"][
                index] + ", " + patient_details["STATE"][index] + ", " + patient_details["COUNTY"][index]
            data["zipcode"] = str(patient_details["ZIP"][index])
            data["gender"] = str(patient_details["GENDER"][index])
            data["race"] = str(patient_details["RACE"][index])
            data["ethnicity"] = patient_details["ETHNICITY"][index]
            data["marital"] = str(patient_details["MARITAL"][index])
            data["dob"] = str(patient_details["BIRTHDATE"][index])
            return data

# print(returnData(""))