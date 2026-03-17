#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a business"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]

customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

@app.route('/contract/<int:id>')
def contract_id(id):
    for contract in contracts:
        if id == contract['id']:
            response_body = contract['contract_information']
            return make_response(response_body, 200, {})
        else:
            response_body = "Information for the contract id not found!"
            return make_response(response_body, 404, {})
        
@app.route('/customer/<customer_name>')
def customer(customer_name):
    if customer_name in customers:
        return make_response("", 204, {})
    else:
        return make_response("Customer not found!", 404, {})

if __name__ == '__main__':
    app.run(port=5555, debug=True)
