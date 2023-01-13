from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user
from . import db
from .models import Post
from .forms import PostForm

writepost_bp = Blueprint('writepost_bp', __name__)

@writepost_bp.route('/writepost/', methods=['GET', 'POST'])
@login_required
def create_post():
    postform = PostForm()
    if postform.validate_on_submit():
        post = Post(title=postform.title.data, posttext=postform.posttext.data, project_id=postform.project_id.data.id, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('/write.html', form=postform, post_to_update=None)


@writepost_bp.route('/editpost/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    postform = PostForm()
    post = Post.query.filter(Post.id == id).first_or_404()
    if post == None:
        return redirect(url_for('main.index'))
    if postform.validate_on_submit():
        post.change_post(id, request.form['title'], request.form['posttext'], request.form['project_id'])
        return redirect(url_for('main.index'))
    postform.posttext.data = post.posttext  #for TextAreaField you have to set value by yourself
    return render_template('/write.html', form=postform, post_to_update=post)


@writepost_bp.route('/deletepost/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    post = Post.query.filter(Post.id == id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted")
    return redirect(url_for('main.index'))
