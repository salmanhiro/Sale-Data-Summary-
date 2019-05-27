import flask
import json
from flask import request, jsonify
import pandas as pd 

#buat bikin endpoint pake flask, isinya json
app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Create some test data for our catalog in the form of a list of dictionaries.
with open('/root/Documents/machine learning tutorial/Car sales/todo-api/json/carsale.json', 'r') as f:
    data = json.load(f)
books = data

#routing
@app.route('/', methods=['GET'])
def home():
    return "Sori webnya jelek, gaada frontendnya, cuma pake flask"
# A route to return all of the available entries in our catalog.
@app.route('/api/carsale.json', methods=['GET'])
def api_all():
    return jsonify(books)
# ntar berarti buka di http://127.0.0.1:5000/api/v1/resources/books/all
app.run()