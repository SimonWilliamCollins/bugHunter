import json
from flask import Flask, request, jsonify
from flask.ext.login import (current_user, loginManager, login_user, logout_user, login_required)
from falsk_

login_manager = loginManager()
login_manager.init_app(app)

app = Flask(__name__)

@app.route('/login', method = ['POST'])
def login():
    info = json.loads(request.data)
    username = info.get()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1'. port=81)