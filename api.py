import flask
from flask import request,jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

familymembers = [
    {'id': 0,
     'Name': 'Deepak',
     'Age': '19',
     'Height': '67"',
     'Weight': '115lbs'},
    {'id': 1,
     'Name': 'Sudarsan',
     'Age': '12',
     'Height': '53"',
     'Weight': '115lbs'},
    {'id': 2,
     'Name': 'Govind',
     'Age': '47',
     'Height': '66"',
     'Weight': '170lbs'},
    {'id': 3,
     'Name': 'Bhuvana',
     'Age': '45',
     'Height': '62"',
     'Weight': '150lbs'}
]

@app.route('/', methods=['GET'])
def home():
    return "Prototype"

# A route to return all of the available entries in the catalog.
@app.route('/api/v1/resources/familymembers/all', methods=['GET'])
def api_all():
    return jsonify(familymembers)

@app.route('/api/v1/resources/familymembers', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id provided"
    results = []

    for member in familymembers:
        if member['id'] == id:
            results.append(member)
    return jsonify(results)


app.run()