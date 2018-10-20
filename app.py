
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sys

# Settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/appdb'
db = SQLAlchemy(app)
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

@app.route('/test2')
def test2():
    b = db.session.execute("select id from post limit 1;").fetchall()
    d, a = {}, []
    for rowproxy in b:
        a = jsonify({"id": rowproxy[0]})
        return a

if __name__ == '__main__':
    app.run()
