from flask import Blueprint, render_template, url_for, redirect, flash, request

from forms import PostForm

import db

writepost_bp = Blueprint('writepost_bp', __name__)

@writepost_bp.route('/writepost/', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    name_to_update = None
    if form.validate_on_submit():
        if not db.save_post(form.title.data, form.content.data):
            flash("Что-то неправильное в данных, наверно где-то пусто", "error")
        else:
            return redirect(url_for('index'))
    return render_template('/write.html', form=form, name_to_update=name_to_update)


@writepost_bp.route('/editpost/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    form = PostForm()
    name_to_update = db.get_post(id)
    if name_to_update == None:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        if db.change_post(id, request.form['title'], request.form['content']):
            return redirect(url_for('index'))
    form.content.data = name_to_update.content
    return render_template('/write.html', form=form, name_to_update=name_to_update)


@writepost_bp.route('/deletepost/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    if db.delete_post(id):
        flash("Пост удален")
    else:
        flash("Пост не удален", error)
    return redirect(url_for('index'))