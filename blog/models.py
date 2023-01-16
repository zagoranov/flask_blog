from datetime import datetime
from flask_login import UserMixin
from . import db


class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    dt = db.Column(db.DateTime, default=datetime.utcnow)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    projects = db.relationship('Project', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    followed = db.relationship('Follow', foreign_keys=[Follow.follower_id], 
                                backref=db.backref('follower', lazy='joined'),
                                lazy='dynamic', 
                                cascade='all, delete-orphan')
    followers = db.relationship('Follow', foreign_keys=[Follow.followed_id], 
                                backref=db.backref('followed', lazy='joined'),
                                lazy='dynamic', 
                                cascade='all, delete-orphan')

    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)
            db.session.commit()

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)
            db.session.commit()

    def is_following(self, user):
        return self.followed.filter_by(followed_id=user.id).first() is not None
    
    def is_followed_by(self, user):
        return self.followers.filter_by(follower_id=user.id).first() is not None

    def __repr__(self):
        return f'<User "{self.id}, {self.name}">'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200))
    deleted = db.Column(db.Boolean, default=False)
    dt = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='project', lazy='dynamic')

    def change_project(self, title, description):
        self.title = title
        self.description = description
        db.session.commit()

    def __repr__(self):
        return f'{self.title}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    title = db.Column(db.String(200), nullable=False)
    posttext = db.Column(db.Text)
    deleted = db.Column(db.Boolean, default=False)
    visibility = db.Column(db.Integer, default=0)
    dt = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='post')

    def change_post(self, title, posttext):
        self.title = title
        self.posttext = posttext
        db.session.commit()

    def __repr__(self):
        return f'<Post: {self.user_id} at {self.dt.strftime("%d/%m/%Y %H:%M:%S")}: "{self.title[:20]}...">'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    dt = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Comment: {self.user_id} at {self.dt.strftime("%d/%m/%Y %H:%M:%S")}: "{self.content[:20]}...">'

