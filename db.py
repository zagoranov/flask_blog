from flask import flash
from main import Post, dbase

def save_post(title, content):
    post = Post(title=title, content=content)
    try:
        dbase.session.add(post)
        dbase.session.commit()
    except:
        flash("Что-то неправильное в данных, наверно где-то пусто", "error")
        return False
    return True

def getPosts():
    return Post.query.all()