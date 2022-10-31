import sys
from crypt import methods
from urllib import request
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

import db

from writepost import writepost_bp

class Post(db.dbase.Model):
    id = db.dbase.Column(db.Integer, primary_key=True)
    title = db.dbase.Column(db.String(200), nullable=False)
    content = db.dbase.Column(db.Text, nullable=False)
    deleted = db.dbase.Column(db.Boolean, default=False)

app = Flask(__name__)

# Регистрируем другие страницы
app.register_blueprint(writepost_bp)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', data=posts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def run():
    if not db.init(app):
        print('Error during creating database connection', file=sys.stderr)


if __name__ == "__main__":
    app.run(debug=True)