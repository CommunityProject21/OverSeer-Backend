from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
import Login

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

if __name__ == '__main__':
    app.run(debug=True)
