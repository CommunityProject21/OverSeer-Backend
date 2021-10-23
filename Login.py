import pandas as pd


def login(UserId, password):
    password_data_path = "./static/DataSets/Login/password.csv"
    data = pd.read_csv(password_data_path)
    stored_password_loc = data[data['Id'] == UserId].index
    stored_password = data.iloc[stored_password_loc]['Password'].values[0]
    return stored_password == password
