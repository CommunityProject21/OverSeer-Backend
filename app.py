from flask import Flask, request, jsonify, abort
from werkzeug.exceptions import BadRequest
from flask_cors import CORS, cross_origin
import jwt
import datetime
from functools import wraps
import numpy as np
import Login
import LoginDoc
import Details
import Allergies
import Implants
import Medications
import Prediction
import Conditions
import Observations
from Training import symptom_info

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'thisissecretone'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        print(request.headers)
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        print("Token:" +str(token))
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'],['HS256'])
            print(data['public_id'])
            current_user = data['public_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message' : 'Token is Expired!'}), 401
        except:
            return jsonify({'message' : 'Token is invalid!'}), 402
        return f(*args, **kwargs)
    return decorated


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
        token = jwt.encode({'public_id' : userId, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'userid': userId, 'login': True, 'usertype': userType, 'token' : token})
    else:
        abort(401)


@app.route('/details', methods=['GET', 'POST', 'OPTIONS'])
@token_required
@cross_origin(supports_credentials=True, origin="*")
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
@token_required
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
@token_required
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
@token_required
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
        prediction_data=Prediction.predictDisease(Symptoms)
        prediction=prediction_data.split("**")
        return jsonify({"prediction":prediction[0], "recommendations":prediction[1]})


@app.route("/conditions", methods=["GET", "POST"])
@token_required
@cross_origin(supports_credentials=True)
def conditions():
    json_data = request.get_json()
    if(json_data['userid']):
        UserId = json_data['userid']
    else:
        handle_bad_request()
    patient_conditions = Conditions.returnData(UserId)
    return jsonify(patient_conditions)


@app.route("/observations", methods=["GET", "POST"])
@token_required
@cross_origin(supports_credentials=True)
def observations():
    json_data = request.get_json()
    if(json_data['userid']):
        UserId = json_data['userid']
    else:
        handle_bad_request()
    patient_observations = Observations.returnData(UserId)
    return jsonify(patient_observations)
      

if __name__ == '__main__':
    app.run(debug=False)
