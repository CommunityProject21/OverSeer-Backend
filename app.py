from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
import Login
import Details
import Allergies
import Implants
import Medications

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def index():
    return 'OverSeer-Backend !!'


@app.route('/login', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def login():
    json_data = request.get_json()
    UserId = json_data['userid']
    password = json_data['password']
    verdict = Login.login(UserId, password)
    if verdict:
        return jsonify({'userid': UserId, 'login': True})
    else:
        abort(401)


@app.route('/details', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def details():
    json_data = request.get_json()
    UserId = json_data['userid']
    patient_data = Details.returnData(UserId)
    if patient_data is None:
        patient_data = {"message": "No such Id"}
    return jsonify(patient_data)


@app.route('/allergies', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def allergies():
    json_data = request.get_json()
    UserId = json_data['userid']
    patient_allergies = Allergies.returnData(UserId)
    return jsonify(patient_allergies)


@app.route('/implants', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def implants():
    json_data = request.get_json()
    UserId = json_data['userid']
    patient_implants = Implants.returnData(UserId)
    return jsonify(patient_implants)


@app.route('/medications', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def medications():
    json_data = request.get_json()
    UserId = json_data['userid']
    patient_medications = Medications.returnData(UserId)
    return jsonify(patient_medications)


if __name__ == '__main__':
    app.run(debug=True)
