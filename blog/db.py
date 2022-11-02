from flask import flash
from datetime import datetime

from main import Post, dbase

def save_post(title, posttext):
    post = Post(title=title, posttext=posttext, dt=datetime.now())
    try:
        dbase.session.add(post)
        dbase.session.commit()
    except:
        flash("Что-то неправильное в данных, наверно где-то пусто", "error")
        return False
    return True


def change_post(id, title, posttext):
    post = Post.query.filter(Post.id == id).first()
    if post == None :
        flash("Что-то неправильное в этом id", "error")
        return False
    try:
        post.title = title
        post.posttext = posttext
        dbase.session.commit()
    except:
        flash("Что-то неправильное с БД", "error")
        return False
    return True


def get_post(id):
    post = Post.query.filter(Post.id == id).first()
    if post == None :
        flash("Что-то неправильное в этом id", "error")
    return post


def delete_post(id):
    post = Post.query.filter(Post.id == id).delete()
    dbase.session.commit()
    return True


def getPosts():
    return Post.query.all()