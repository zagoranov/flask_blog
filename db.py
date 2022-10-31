from flask_sqlalchemy import SQLAlchemy

def init(app):
    try:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        dbase = SQLAlchemy(app)
        dbase.init_app(app)
        return True
    except:
        return False
