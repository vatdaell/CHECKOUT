from flask import Flask,request
from porc import Client
API_KEY = '16509990-f7fc-48dc-b128-716c99b65a24'
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




if __name__ == '__main__':
    app.run(host = '0.0.0.0')

