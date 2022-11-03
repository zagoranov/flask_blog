# Blog: test project 
flask + sqlalchemy + bootstrap

## _Based on_
- Base: https://www.youtube.com/watch?v=759C2p3CAA4
- Forms: https://www.youtube.com/watch?v=oba6GGprvKc
- Authentication: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

## _To create db_
```console
python
>>> from blog import db, create_app, models
>>> db.create_all(app=create_app())
exit()

```

## Env stuff
```console
python3 -m venv blog
source blog/bin/activate
export FLASK_APP=blog
export FLASK_DEBUG=1
```

## Requires
- Flask
- flask-sqlalchemy
- flask_wtf
- flask_login
