import os
from crypt import methods
from urllib import request
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, Text

import db

from writepost import writepost_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


dbase = SQLAlchemy(app)
dbase.init_app(app)

class Post(dbase.Model):
    id = dbase.Column(Integer, primary_key=True)
    title = dbase.Column(String(200), nullable=False)
    content = dbase.Column(Text, nullable=False)
    deleted = dbase.Column(Boolean, default=False)

# Регистрируем другие страницы
app.register_blueprint(writepost_bp)

@app.route('/')
def index():
    posts = db.getPosts()
    return render_template('index.html', data=posts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


#def run():
#    if not db.init(app):
#        print('Error during creating database connection', file=sys.stderr)


if __name__ == "__main__":
    app.run(debug=True)