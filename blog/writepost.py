from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_required
from .forms import PostForm

from .dbase import *

writepost_bp = Blueprint('writepost_bp', __name__)

@writepost_bp.route('/writepost/', methods=['GET', 'POST'])
@login_required
def create_post():
    postform = PostForm()
    if postform.validate_on_submit():
        if not save_post(postform.title.data, postform.posttext.data):
            flash("Something bad of empty with data", "error")
        else:
            return redirect(url_for('main.index'))
    return render_template('/write.html', form=postform, post_to_update=None)


@writepost_bp.route('/editpost/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    postform = PostForm()
    post_to_update = get_post(id)
    if post_to_update == None:
        return redirect(url_for('main.index'))
    if postform.validate_on_submit():
        if change_post(id, request.form['title'], request.form['posttext']):
            return redirect(url_for('main.index'))
    postform.posttext.data = post_to_update.posttext  #for TextAreaField you have to set value by yourself
    return render_template('/write.html', form=postform, post_to_update=post_to_update)


@writepost_bp.route('/deletepost/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    if delete_post(id):
        flash("Post deleted")
    else:
        flash("Post not deleted", 'error')
    return redirect(url_for('main.index'))