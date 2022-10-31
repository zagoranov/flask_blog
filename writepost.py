from flask import Blueprint, render_template, redirect, url_for, request

import db
from forms import PostForm

writepost_bp = Blueprint('writepost_bp', __name__)

@writepost_bp.route('/', methods=['GET', 'POST'])
def write_post():
        form = PostForm()
        if form.validate_on_submit():
            post = Post(title=form.title.data, content=form.content.data)
            try:
                db.dbase.session.add(post)
                db.dbase.session.commit()
            except:
                return "Получилась ошибка!"
            return redirect('/')
        flash("Что-то неправильное в данных, наверно где-то пусто", "error")

    return render_template('/write.html', form=form)
