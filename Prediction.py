from flask import Flask, render_template, request
import pickle
import numpy as np
from Training import data_dict
from statistics import mode


def predictDisease(symptoms):
    file = open("./Models/svm_model.pkl", "rb")
    svm_model = pickle.load(file)
    file.close()

    file = open("./Models/nb_model.pkl", "rb")
    nb_model = pickle.load(file)
    file.close()

    file = open("./Models/rf_model.pkl", "rb")
    rf_model = pickle.load(file)
    file.close()

    
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
        
    # reshaping the input data and converting it
    # into suitable format for model predictions
    input_data = np.array(input_data).reshape(1,-1)
    
    # generating individual outputs
    rf_prediction = data_dict["predictions_classes"][rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][svm_model.predict(input_data)[0]]
    
    # making final prediction by taking mode of all predictions
    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])
    return final_prediction

