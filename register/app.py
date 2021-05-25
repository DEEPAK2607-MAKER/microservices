from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify, request

from datetime import datetime

from dateutil.relativedelta import relativedelta

from random import randint

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/local"

mongo = PyMongo(app)


@app.route('/api/v1/sendmail', methods=['GET', 'POST'])
def senddetails():
    _json = request.json
    _customername = _json['customer name']
    _customerid = _json['customer id']

    print(_customerid, _customername)

    id = mongo.db.local.insert_one({'customer name': _customername, 'customer id': _customerid})

    return "success"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
