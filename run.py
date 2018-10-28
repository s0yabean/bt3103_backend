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

# # Mother of all functions
# @app.route('/<mod_id>/<chart>')
# def mother_function(mod_id, chart):
#     if chart == 'diff_spd':
#         code = "'" + mod_id + "'"
#         query = 'select round(avg(m2), 2) as value from official_reviews where mod_class_id=' + code 
#         a = run_sql(query)
#     if chart == 'snt_spd':
#         code = "'" + mod_id + "'"
#         query = 'select round(avg(SUBSTRING(m4c,11,2)::int + SUBSTRING(m5c,10,2)::int), 2) as value from official_reviews where mod_class_id=' + code
#         a = run_sql(query)
#     return Response(json.dumps(a), mimetype='application/json')

# Mother of all functions
@app.route('/<mod_id>/<chart>')
def mother_function(mod_id, chart):

    if chart == 'diff_spd': #difficulty level speedometer
        code = "'" + mod_id + "'"
        query = 'select round(avg(m2), 2) as value from official_reviews where mod_class_id=' + code 
        a = run_sql(query)

    if chart == 'snt_spd': #sentiment speedometer
        code = "'" + mod_id + "'"
        query = 'select round(avg((SUBSTRING(m4c,11,2)::int + SUBSTRING(m5c,10,2)::int)/2),2) as value from official_reviews where mod_class_id=' + code
        a = run_sql(query)
    
    if chart == 'overall_1': #overall opinion  (poor)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as count from official_reviews where m1=1 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'overall_2': #overall opinion  (unsatisfactory)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as count from official_reviews where m1=2 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'overall_3': #overall opinion  (satisfactory)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as count from official_reviews where m1=3 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'overall_4': #overall opinion  (good)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as count from official_reviews where m1=4 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'overall_5': #overall opinion  (excellent)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as count from official_reviews where m1=5 and mod_class_id=' + code
        a = run_sql(query)
    
    if chart == 'exp_1': #expected grade (A)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as Expected_Count from official_reviews where m2=1 and mod_class_id=' + code
        a = run_sql(query)
  
    if chart == 'exp_2': #expected grade (B)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as Expected_Count from official_reviews where m2=2 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'exp_3': #expected grade (C)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as Expected_Count from official_reviews where m2=3 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'exp_4': #expected grade (D)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as Expected_Count from official_reviews where m2=4 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'exp_5': #expected grade (F)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as Expected_Count from official_reviews where m2=5 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'act_1': #actual grade (A)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as actual_count from official_reviews where actual_grade=1 and mod_class_id=' + code
        a = run_sql(query)
  
    if chart == 'act_2': #actual grade (B)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as actual_count from official_reviews where actual_grade=2 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'act_3': #actual grade (C)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as actual_count from official_reviews where actual_grade=3 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'act_4': #actual grade (D)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as actual_count from official_reviews where actual_grade=4 and mod_class_id=' + code
        a = run_sql(query)

    if chart == 'act_5': #actual grade (F)
        code = "'" + mod_id + "'"
        query = 'Select count(review_id) as actual_count from official_reviews where actual_grade=5 and mod_class_id=' + code
        a = run_sql(query)

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
