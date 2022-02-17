# Importing libraries
import numpy as np
import pandas as pd
from scipy.stats import mode
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


df = pd.read_csv("Training.csv")
symptoms = list(df.columns)
df = df.drop(columns = "Unnamed: 133" , axis=1)

encoder = LabelEncoder()
df["prognosis"] = encoder.fit_transform(df["prognosis"])

X = df.iloc[:,:-1]
Y = df.iloc[:, -1]
X_Train, X_Test, Y_Train, Y_Test =train_test_split(X, Y, test_size = 0.2, random_state = 2)

# Training and testing SVM Classifier
svm_model = SVC()
svm_model.fit(X_Train, Y_Train)

# Training and testing Naive Bayes Classifier
nb_model = GaussianNB()
nb_model.fit(X_Train, Y_Train)

# Training and testing Random Forest Classifier
rf_model = RandomForestClassifier(random_state=18)
rf_model.fit(X_Train, Y_Train)

# open a file where you want to store the data 
file  = open("svm_model.pkl", "wb")

# dump information to that file
pickle.dump(svm_model, file)

file.close()

file  = open("nb_model.pkl", "wb")
pickle.dump(nb_model, file)
file.close()

file  = open("rf_model.pkl", "wb")
pickle.dump(rf_model, file)
file.close()


symptoms = X.columns.values

# Creating a symptom index dictionary to encode the
# input symptoms into numerical form
symptom_index = {}
symptom_info=[]
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_info.append(symptom)
    symptom_index[symptom] = index

data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":encoder.classes_
}
