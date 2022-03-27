import pandas as pd
import numpy as np
from Password import RandomPassword as rp

patients_file_path = './static/DataSets/Details/doctor.csv'
password_file_path = './static/DataSets/Login/passwordDoc.csv'

# Feature to add that it checks the ID existing in the password table and for the ones that are not add new password entries for them. 

patients = pd.read_csv(patients_file_path)
data = []
for Id in patients['docid']:
    password = rp.generatePassword()
    data.append([Id, password])

password_data = pd.DataFrame(data, columns=['DocId', 'Password'])
password_data.to_csv(password_file_path);
