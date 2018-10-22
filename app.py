
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import requests
import json
import sys

# Settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ytsnozrropwoym:611808c63f96c74d7b755cebc8857cabac5b94215097046256d8cd6855323254@ec2-174-129-236-147.compute-1.amazonaws.com:5432/d7qvs0a0ed4uf'
db = SQLAlchemy(app)
engine = create_engine('postgresql://ec2-174-129-236-147.compute-1.amazonaws.com:5432/d7qvs0a0ed4uf')

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)

    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def __init__(self, id, title, post_text):
        self.id = id
        self.title = title
        self.post_text = post_text

class official_reviews(db.Model):
    __tablename__ = 'official_reviews'

    review_id = db.Column(db.String(100), primary_key=True)
    student_token = db.Column(db.String(80))
    m1 = db.Column(db.Integer())
    m2 = db.Column(db.Integer())
    m3 = db.Column(db.Integer())
    m4c = db.Column(db.Integer())
    m5c = db.Column(db.Integer())
    mod_class_id = db.Column(db.String(80))
    mod_class_name = db.Column(db.String(255))
    mod_term = db.Column(db.Integer())
    mod_ay = db.Column(db.Integer())
    mod_sem = db.Column(db.Integer())
    mod_rptterm = db.Column(db.Integer())
    mod_module_code = db.Column(db.Integer())

    def __init__(self, review_id, student_token, m1, m2, m3, m4c, m5c, mod_class_id, mod_class_name, mod_term, mod_ay, mod_sem ,mod_rptterm, mod_module_code):
        
        self.review_id = review_id
        self.student_token = student_token
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4c = m4c
        self.m5c = m5c
        self.mod_class_id = mod_class_id
        self.mod_class_name = mod_class_name
        self.mod_term = mod_term
        self.mod_ay = mod_ay
        self.mod_sem = mod_sem
        self.mod_rptterm = mod_rptterm
        self.mod_module_code = mod_module_code

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/js')
def js():
    return jsonify('{"id": 5}, {"id": 5}') 

@app.route('/js2')
def js2():
    return jsonify({"id": 5}, {"id": 5}) 

@app.route('/<user_id>')
def hello_module(user_id):
    return 'Hello ' +  user_id
   
@app.route('/addpost') 
def add_post():
    db.session.add(Post(id = 2, title = 'hello', post_text = 'hello world' ))
    db.session.commit()
    return 'sent to database'

@app.route('/test')
def test():
    b = db.session.execute("select id from post;").fetchall()
    a = ''
    for rowproxy in b:
        a = a + ',' + {"id": rowproxy[0]}.__str__()
    a = a[1:]    
    return jsonify(a)

@app.route('/test2')
def test2():
    b = db.session.execute("select count(*) from official_reivews;").fetchall()
    d, a = {}, []
    for rowproxy in b:
        a = jsonify({"id": rowproxy[0]}) # for now is 1 string and 1 value
    return a

@app.route('/')
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
    return 'Chart code not found!'


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
