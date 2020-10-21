from flask import Flask,request
from porc import Client

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,merchant_id="MERCHANT_ID",public_key="PUBLIC_KEY",private_key="PRIVATE_KEY")



API_KEY = 'API_KEY'
client = Client(API_KEY)



app = Flask(__name__)

@app.route('/price', methods = ['GET', 'POST'])
def price():
	 store = request.args.get('store')
	 upc_code = request.args.get('upc')
	 result = 'No Product In Database'
	 response = client.get('stores',store)
	 if(upc_code in response['upc']):
	 	result =  str(response['upc'][upc_code]['price']) 
	 return result

@app.route('/name', methods = ['GET', 'POST'])
def name():
	 store = request.args.get('store')
	 upc_code = request.args.get('upc')
	 result = 'No Product In Database'
	 response = client.get('stores',store)
	 if(upc_code in response['upc']):
	 	result =  str(response['upc'][upc_code]['name']) 
	 return result


@app.route('/user', methods = ['GET', 'POST'])
def user():
	 username = request.args.get('username')
	 password = request.args.get('password')
	 
	 result = False

	 users_check = client.get('users',username)

	 if(users_check['email'] == username and users_check['password'] == password):
	 	result = True

	 return str(result)

@app.route("/client_token", methods=["GET"])
def client_token():
  return braintree.ClientToken.generate()


@app.route("/checkout", methods=["GET"])
def create_purchase():
	price = request.args.get('price')
	result = braintree.Transaction.sale({"amount": price,"payment_method_nonce": "fake-valid-nonce"})
	return str(result)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
