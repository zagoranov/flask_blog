from flask import Blueprint, render_template, url_for, redirect, flash

from forms import PostForm

import db

writepost_bp = Blueprint('writepost_bp', __name__)

@writepost_bp.route('/writepost/', methods=['GET', 'POST'])
def write_post():
    form = PostForm()
    if form.validate_on_submit():
        if not db.save_post(form.title.data, form.content.data):
            flash("Что-то неправильное в данных, наверно где-то пусто", "error")
        else:
            return redirect(url_for('index'))

    return render_template('/write.html', form=form)
