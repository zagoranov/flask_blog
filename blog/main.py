from flask import Blueprint, render_template
from flask_login import login_required, current_user
#from . import db
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

