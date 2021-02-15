import json
from flask import Flask, request, jsonify
from flask.ext.login import (current_user, loginManager, login_user, logout_user, login_required)
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGOB_SETTING'] = {
    'db': 'userAccounts',
    'host': 'localhost',
    'port': '27017'
}

app.secret_key = 'rdffH3455'
db = MongoEngine()
login_manager = loginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()
@app.route('/login', methods=['POST'])
def login():
    info = json.loads(request.data)
    username = info.get('username', 'guest')
    password = info.get('password', '')
    user = user.objects(name=username, password=password).first()

    if users:
        login_user(user)
        return jsonify(user.to_json())
    else:
        return jsonify({"status": 401,
                        "reason": "Username or Password Error"})
@app.route('/logout', method = ['POST'])
def logout():
    logout_user()
    return jsonify(**{'result': 200,
                        'data': {'message': 'Logout succuss'}})
@app.route('/user_info', methods=['POST'])
def user_info():
    if current_user.is_authenticated:
        reap = {"result": 200,
                "data": current_user.to_json()}
    else:
        resp = {"result": 401,
                "data": {"message": "user no login"}}

    return jsonify(**resp)

class User(db.Document):
    name = db.StringField()
    password = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}
    

@app.route('/login', method = ['POST'])
def login():
    info = json.loads(request.data)
    username = info.get()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1'. port=81)