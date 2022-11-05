from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Post, Comment
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', data=posts)

@main.route('/writecomment/', methods=['POST'])
@login_required
def create_comment():
    comment = Comment(content=request.form['comment'], user_id=current_user.id, post_id=request.form['post_id'])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.index'))
