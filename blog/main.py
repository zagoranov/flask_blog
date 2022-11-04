from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .models import User
from .dbase import *

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = getPosts()
    return render_template('index.html', data=posts)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/author/<int:id>')
def author_profile(id):
    user = User.query.filter(User.id == id).first_or_404()
    return render_template('profile.html', name=user.name)

@main.route('/writecomment/', methods=['POST'])
@login_required
def create_comment():
    if not save_comment(request.form['comment'], request.form['post_id']):
            flash("Something bad of empty with data", "error")
    return redirect(url_for('main.index'))
