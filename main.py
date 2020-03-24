from flask import Flask, render_template
import os
from mathcloudfunctions import get_multiplication_facts
from decimaltobinary import convert_decimal_to_binary

print("Entering main.py...")
app = Flask(__name__)

@app.route('/')
def process_request_1():
    print("Calling get_multiplication_facts with no arguments.")
    return get_multiplication_facts("", "")

@app.route('/table_of/<str_table_of>')
def process_request_2(str_table_of):
    print("Calling get_multiplication_facts with 1 argument: table_of({}).".format(str_table_of))
    return get_multiplication_facts(str_table_of, "")

@app.route('/limit/<str_limit>')
def process_request_3(str_limit):
    print("Calling get_multiplication_facts with 1 argument: limit({}).".format(str_limit))
    return get_multiplication_facts("", str_limit)

@app.route('/table_of/<str_table_of>/limit/<str_limit>')
def process_request_4(str_table_of, str_limit):
    print("Calling get_multiplication_facts with 2 arguments: table_of({}); limit({}).".format(str_table_of,str_limit))
    return get_multiplication_facts(str_table_of, str_limit)

@app.route('/d2b/<decimal_number>')
def decimal_to_binary_route(decimal_number):
    print("Enterning decimal_to_binary_route...")
    return convert_decimal_to_binary(decimal_number)

if __name__ == "__main__":
    print("Starting MathGarage Python Flask App on Port 5000...")
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0',port=port)