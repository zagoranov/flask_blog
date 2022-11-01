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


def change_post(id, title, content):
    post = Post.query.filter(Post.id == id).first()
    if post == None :
        flash("Что-то неправильное в этом id", "error")
        return False
    try:
        post.title = title
        post.content = content
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