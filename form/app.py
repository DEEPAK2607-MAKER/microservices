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

@app.route('/add', methods=['POST'])

def add_admin():
     _json =request.json
     _customername = _json['customer name']
     _customerid= _json['customer id']
     _customeraddress = _json['customer address']
     _customerphonenumber = _json['customer phone number']
     _customeracctype = _json['customer acc type']
     _amount = int(_json['amount'])
     _interest = int(_json['interest'])
     _year = int(_json['year'])
     _term = int(_json['term'])
     # randomdate = random_with_N_digits(3)

     # print(orderdd)

     # today = datetime.utcnow().strftime('%Y-%m-%d ')
     #
     # today = datetime.now() + relativedelta(years=4 , days=5)
     #
     # print (today)

     if  request.method =='POST':

         if (_customername and _customerid and _customeraddress and _customerphonenumber and _customeracctype and _amount and _interest and _year and _term):

              if (len(_customername) <= 6) :

                api_url = "http://192.168.0.104:5002/api/v1/req"
                data = {'customer name': _customername, 'customer id': _customerid }
                requests.post(url=api_url, json=data)
                id = mongo.db.admin.insert_one({'customer name': _customername, 'customer id': _customerid , 'customer address': _customeraddress ,
                                         'customer phone number': _customerphonenumber, 'customer acc type': _customeracctype, 'amount': _amount, "interest": _interest, "year": _year, "term": _term})

                resp = jsonify("user added successfully")

                resp.status_code = 200

                return resp

              else :

                  return "charcter exceeds"

         else :

             return "Arguments missing"
     else:
         return "missing aarguments"




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug = True)