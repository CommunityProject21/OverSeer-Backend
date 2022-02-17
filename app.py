from flask import Flask, request, jsonify, abort
from werkzeug.exceptions import BadRequest
from flask_cors import CORS, cross_origin
import numpy as np
import Login
import LoginDoc
import Details
import Allergies
import Implants
import Medications
import Prediction
from Training import symptom_info

app = Flask(__name__)

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400


@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def index():
    return 'OverSeer-Backend !!'


@app.route('/login', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def login():
    json_data = request.get_json()
    if(json_data['userid'] and json_data['password'] and json_data['usertype'] ):
        userId = json_data['userid']
        password = json_data['password']
        userType = json_data['usertype']
    else:
        handle_bad_request()
    if(userType == 'P'):
        verdict = Login.login(userId, password)
    else:
        verdict = LoginDoc.login(userId,password)
    if verdict:
        return jsonify({'userid': userId, 'login': True, 'usertype': userType})
    else:
        abort(401)


@app.route('/details', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def details():
    json_data = request.get_json()
    if(json_data['userid']):
        UserId = json_data['userid']
    else:
        handle_bad_request()
    patient_data = Details.returnData(UserId)
    if patient_data is None:
        patient_data = {"message": "No such Id"}
    return jsonify(patient_data)


@app.route('/allergies', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def allergies():
    json_data = request.get_json()
    if(json_data['userid']):
        UserId = json_data['userid']
    else:
        handle_bad_request()
    patient_allergies = Allergies.returnData(UserId)
    return jsonify(patient_allergies)


@app.route('/implants', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def implants():
    json_data = request.get_json()
    if(json_data['userid']):
        UserId = json_data['userid']
    else:
        handle_bad_request()
    patient_implants = Implants.returnData(UserId)
    return jsonify(patient_implants)


@app.route('/medications', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def medications():
    json_data = request.get_json()
    if(json_data['userid']):
        UserId = json_data['userid']
    else:
        handle_bad_request()
    patient_medications = Medications.returnData(UserId)
    return jsonify(patient_medications)


@app.route("/predictions", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def predictions():
    if(request.method =='GET'):
        Symptoms = symptom_info
        return jsonify({"symptom-list":Symptoms})
    if(request.method == 'POST'):
        json_data = request.get_json()
        if(json_data['symptoms']):
            Symptoms = json_data['symptoms']
        else:
            handle_bad_request()
        prediction=Prediction.predictDisease(Symptoms)
        return jsonify({"prediction":prediction})

if __name__ == '__main__':
    app.run(debug=True)
