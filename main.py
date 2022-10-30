from crypt import methods
from urllib import request
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    deleted = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', data=posts)

@app.route('/write', methods=['GET', 'POST'])
def write_post():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content)
        try:
            db.session.add(post)
            db.session.commit()
        except:
            return "Получилась ошибка!"
        return redirect('/')
    else:
        return render_template('/write.html')


if __name__ == "__main__":
    app.run(debug=True)