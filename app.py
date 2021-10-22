from flask import Flask
from Password import RandomPassword as RP

app = Flask(__name__)


@app.route('/')
def index():
    print(RP.generatePassword())
    return 'OverSeer-Backend !!'


if __name__ == '__main__':
    app.run(debug=True)
