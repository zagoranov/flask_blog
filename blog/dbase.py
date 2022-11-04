from flask import flash
from flask_login import current_user
from datetime import datetime
from . import db
from .models import Post, Comment

def save_post(title, posttext):
    post = Post(title=title, posttext=posttext, dt=datetime.now(), user_id=current_user.id)
    try:
        db.session.add(post)
        db.session.commit()
    except:
        flash("Что-то неправильное в данных, наверно где-то пусто", "error")
        return False
    return True


def change_post(id, title, posttext):
    post = Post.query.filter(Post.id == id).first_or_404()
    if post == None :
        flash("Что-то неправильное в этом id", "error")
        return False
    try:
        post.title = title
        post.posttext = posttext
        db.session.commit()
    except:
        flash("Что-то неправильное с БД", "error")
        return False
    return True


def get_post(id):
    post = Post.query.filter(Post.id == id).first_or_404()
    if post == None :
        flash("Что-то неправильное в этом id", "error")
    return post


def delete_post(id):
    post = Post.query.filter(Post.id == id).delete()
    db.session.commit()
    return True


def getPosts():
    return Post.query.all()


def save_comment(content, post_id):
    comment = Comment(content=content, dt=datetime.now(), user_id=current_user.id, post_id=post_id)
    try:
        db.session.add(comment)
        db.session.commit()
    except:
        flash("Что-то неправильное в данных, наверно где-то пусто", "error")
        return False
    return True
