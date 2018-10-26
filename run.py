
from flask import Flask, request, jsonify
import requests
import json
import sys

# Settings
app = Flask(__name__)
from models import db, create_engine
# Above line needs to be after app is created as models.py needs app. 
# Somewhat a circular dependency but done to make files more compact

from flask import Response

@app.route("/hello")
def route1():
    dict1 = {"prop1": "p1", "prop2": "p2"}
    return Response(json.dumps(dict1), mimetype='application/json')

# Routes 
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<user_id>')
def hello_module(user_id):
    return 'Hello ' +  user_id

@app.route('/test')
def test():
    resultproxy = db.session.execute("select count(*), avg(m1) from official_reviews;").fetchall()
    d, a = {}, {}
    for rowproxy in resultproxy:
        for tup in rowproxy.items():
            d = {**d, **{tup[0]: tup[1]}}
        a.update(d)
    return Response(json.dumps(a), mimetype='application/json')

@app.route('/test4')
def test4():
    resultproxy = db.session.execute("select count(*), avg(m1)  from official_reviews;").fetchall()
    d, a = {}, {}
    for rowproxy in resultproxy:
        for tup in rowproxy.items():
            d = {**d, **{tup[0]: tup[1]}}
    a.update(d)
    return Response(json.dumps(a), mimetype='application/json')

@app.route('/<mod_id>/<chart>')
def avgm1(mod_id, chart):
    if chart == 'avgm1':
        code = "'" + mod_id + "'"
        query = "select avg(m1) from official_reviews where mod_class_id = " + code
        b = db.session.execute(query).fetchall()
        a = ''
        for rowproxy in b:
            a = a + ',' + {"id": rowproxy[0]}.__str__()
            a = a[1:]    
        return jsonify(a)

if __name__ == '__main__':
    app.run()
