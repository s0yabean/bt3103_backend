
from flask import Flask, request, render_template, jsonify
import requests
import json
import sys

# Settings
app = Flask(__name__)
from models import db, create_engine
# Above line needs to be after app is created as models.py needs app. 
# Somewhat a circular dependency but done to make files more compact

# Routes 
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<user_id>')
def hello_module(user_id):
    return 'Hello ' +  user_id

@app.route('/test2')
def test2():
    b = db.session.execute("select count(*) from official_reviews;").fetchall()
    d, a = {}, []
    for rowproxy in b:
        a = jsonify({"id": rowproxy[0]}) # for now is 1 string and 1 value
    return a

@app.route('/test3')
def test3():
    b = db.session.execute("select id from post;").fetchall()
    d, a = {}, []
    for rowproxy in b:
        a = jsonify({"id": rowproxy[0]}) # for now is 1 string and 1 value
    return a
    
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
    #return jsonify(query)
    #return 'Chart code not found!'

@app.route('/update')
def update():
    incrementFirebaseCounter()
    return 'updated firebase!'

def incrementFirebaseCounter():
  resp = requests.get(url="https://bt3103-final-project.herokuapp.com/test2")
  value = json.loads(resp.text)['id']
  value = value
  resp2 = requests.put(url = 'https://bt3103-review-for-review.firebaseio.com/id.json', data = json.dumps({'id':value}))

if __name__ == '__main__':
    app.run()
