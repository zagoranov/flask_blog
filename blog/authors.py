from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user
from .models import User
from .forms import UserForm

authors = Blueprint('authors', __name__)

@authors.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    userform = UserForm()
    user = User.query.filter(User.id == current_user.id).first_or_404()
    if userform.validate_on_submit():
        current_user.change_user(request.form['name'])
        return redirect(url_for('main.index'))
    return render_template('profile.html', form=userform, user=user)

@authors.route('/author/<int:id>')
def author_profile(id):
    user = User.query.filter(User.id == id).first_or_404()
    return render_template('profile.html', user=user)

@authors.route('/follow/<int:id>')
@login_required
def follow(id):
    user = User.query.filter(User.id == id).first_or_404()
    if current_user.is_following(user):
        flash('You already following %s', user.name)
    else:
        current_user.follow(user)
        flash('You now following %s', user.name)
    return render_template('profile.html', user=user)

@authors.route('/unfollow/<int:id>')
@login_required
def unfollow(id):
    user = User.query.filter(User.id == id).first_or_404()
    if current_user.is_following(user):
        current_user.unfollow(user)
        flash('You unfollowed %s', user.name)
    else:
        flash('You are not followed %s', user.name)
    return render_template('profile.html', user=user)

