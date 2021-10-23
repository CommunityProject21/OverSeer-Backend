import pandas as pd
import numpy as np
from Password import RandomPassword as rp

patients_file_path = './static/DataSets/Details/patients.csv'
password_file_path = './static/DataSets/Login/password.csv'

patients = pd.read_csv(patients_file_path)
data = []
for Id in patients['Id']:
    password = rp.generatePassword()
    data.append([Id, password])

password_data = pd.DataFrame(data, columns=['Id', 'Password'])
password_data.to_csv(password_file_path);

