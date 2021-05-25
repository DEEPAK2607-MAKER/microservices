from  flask import Flask

from flask_pymongo import PyMongo

from bson.json_util  import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from datetime import datetime

from dateutil.relativedelta import relativedelta

from random import randint

# from pip._vendor import requests

import requests


from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/admin"

mongo = PyMongo(app)


@app.route('/api/v1/req', methods = ['GET', 'POST'])
def req():
    # _json = request.json
    _customername = request.json['customer name']
    _customerid = request.json['customer id']
    # _customeraddress = _json['customer address']
    # _customerphonenumber = _json['customer phone number']
    # _customeracctype = _json['customer acc type']
    # _amount = int(_json['amount'])
    # _interest = int(_json['interest'])
    # _year = int(_json['year'])
    # _term = int(_json['term'])

    print(_customername)
    api_url = "http://192.168.0.104:5003/api/v1/sendmail"

    data ={ 'customer name': _customername, 'customer id': _customerid }





    txn = requests.post(url=api_url,json=data)


    return "success"

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=5002)
