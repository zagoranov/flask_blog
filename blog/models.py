from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = db.relationship('Post', backref='user')
    comments = db.relationship('Comment', backref='user')

    def __repr__(self):
        return f'<User "{self.id}, {self.name}">'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(200), nullable=False)
    posttext = db.Column(db.Text)
    deleted = db.Column(db.Boolean, default=False)
    dt = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='post')

    def __repr__(self):
        return f'<Post: {self.user_id} at {self.dt.strftime("%d/%m/%Y %H:%M:%S")}: "{self.title[:20]}...">'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    dt = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Comment: {self.user_id} at {self.dt.strftime("%d/%m/%Y %H:%M:%S")}: "{self.content[:20]}...">'
