
from flask import Flask, request, jsonify
import simplejson as json
import requests
#import json
import sys

# Settings
app = Flask(__name__)
from models import db, create_engine
# Above line needs to be after app is created as models.py needs app. 
# Somewhat a circular dependency but done to make files more compact

from flask import Response

# Function to run SQL query and take output
def run_sql(query):
    resultproxy = db.session.execute(query).fetchall()
    d, a = {}, {}
    for rowproxy in resultproxy:
        for tup in rowproxy.items():
            d = {**d, **{tup[0]: tup[1]}}
        a.update(d)
    return a

# Routes 
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    resultproxy = db.session.execute("select round(avg(m2), 2) as value from official_reviews;").fetchall()
    d, a = {}, {}
    for rowproxy in resultproxy:
        for tup in rowproxy.items():
            d = {**d, **{tup[0]: tup[1]}}
        a.update(d)
    return Response(json.dumps(a), mimetype='application/json')    

# Mother of all functions
@app.route('/<mod_id>/<chart>')
def mother_function(mod_id, chart):
    if chart == 'exp_grade':
        code = "'" + mod_id + "'"
        query = 'select m2, count(review_id) from official_reviews where mod_class_id=' + code + ' group by m2;'
        run_sql(query)
    return Response(json.dumps(a), mimetype='application/json')

if __name__ == '__main__':
    app.run()


#Resultproxy docs:
#class sqlalchemy.engine.RowProxy(parent, row, processors, keymap)
#Proxy values from a single cursor row.
#Mostly follows “ordered dictionary” behavior, mapping result values to the string-based column name, the integer position of the result in the row, as well as Column instances which can be mapped to the original Columns that produced this result set (for results that correspond to constructed SQL expressions).
#has_key(key) Return True if this RowProxy contains the given key.
#items() Return a list of tuples, each tuple containing a key/value pair.
#keys() Return the list of keys as strings represented by this RowProxy.
#https://stackoverflow.com/questions/20743806/sqlalchemy-execute-return-resultproxy-as-tuple-not-dict
