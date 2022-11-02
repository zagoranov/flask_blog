from flask import Blueprint, render_template, url_for, redirect, flash, request

from forms import PostForm

import db

writepost_bp = Blueprint('writepost_bp', __name__)

@writepost_bp.route('/writepost/', methods=['GET', 'POST'])
def create_post():
    postform = PostForm()
    if postform.validate_on_submit():
        if not db.save_post(postform.title.data, postform.posttext.data):
            flash("Что-то неправильное в данных, наверно где-то пусто", "error")
        else:
            return redirect(url_for('index'))
    return render_template('/write.html', form=postform, post_to_update=None)


@writepost_bp.route('/editpost/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    postform = PostForm()
    post_to_update = db.get_post(id)
    if post_to_update == None:
        return redirect(url_for('index'))
    if postform.validate_on_submit():
        if db.change_post(id, request.form['title'], request.form['posttext']):
            return redirect(url_for('index'))
    postform.posttext.data = post_to_update.posttext  #for TextAreaField you have to set value by yourself
    return render_template('/write.html', form=postform, post_to_update=post_to_update)


@writepost_bp.route('/deletepost/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    if db.delete_post(id):
        flash("Пост удален")
    else:
        flash("Пост не удален", error)
    return redirect(url_for('index'))