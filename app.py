
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sys
import psycopg2

# Settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/appdb'
db = SQLAlchemy(app)
conn = psycopg2.connect('postgresql://localhost/appdb')
engine = create_engine('postgresql://localhost/appdb')

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def __init__(self, id, title, post_text):
        self.id = id
        self.title = title
        self.post_text = post_text


@app.route('/')
def hello_world():
    return 'Hello, World!'

#@app.route('/addpost', methods=['GET', 'POST'])
@app.route('/addpost')
def add_post():
    db.session.add(Post(id = 2, title = 'hello', post_text = 'hello world' ))
    db.session.commit()
    return 'sent to database'

@app.route('/testvue')
def test_vue():
    return render_template('get_vue.html')

@app.route('/test')
def test():
    #con = engine.cursor()
   
    b = db.session.execute("select id from post limit 1;").fetchall()
    #below works
    #b = con.execute('select id from post limit 1;').fetchall()
    #con.close()
    cursor = conn.cursor()
    cursor.execute('ROLLBACK')
    cursor.execute("SELECT id FROM post;")
    records = cursor.fetchall()
   
    #for row in records:
    #    return dict(row)
    d, a = {}, []
    for rowproxy in records:
        a = jsonify({"id": rowproxy[0]})
        return a
        #returns an array like [(key0, value0), (key1, value1)]
        #build up the dictionary
       # d = {**d, **{rowproxy[0]: rowproxy[0]}}
   # a.append(d)
    
    #for row in b:
    #    d = row['id']
        #d['Tags'] = d['Keywords']

    #result = {
    #"isBase64Encoded": False,
    #"statusCode": 200,
    #"headers": {},
    #"body": records[1]
   #}
 
    #return app.response_class(jsonify(result), content_type='application/json')
    #app.response_class(records, content_type='application/json')
   # app.response_class(a, content_type='application/json')
    #jsonify(d)
    

if __name__ == '__main__':
    app.run()
