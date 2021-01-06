from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
   user = request.form['nm']
   
   resp = Flask.make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome ' + name + '<h1>'



if __name__ == '__main__':
    app.run(debug=True)