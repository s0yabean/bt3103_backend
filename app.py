
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
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


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/addpost')
def add_post():
    db.session.add(Post(id = 2, title = 'hello', post_text = 'hello world' ))
    db.session.commit()
    return 'sent to database'

@app.route('/test2')
def test2():
    b = db.session.execute("select id from post limit 1;").fetchall()
    d, a = {}, []
    for rowproxy in b:
        a = jsonify({"id": rowproxy[0]})
        return a

if __name__ == '__main__':
    app.run()
