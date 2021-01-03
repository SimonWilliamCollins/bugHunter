from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    users = ['Helen', 'Adrianna', 'Victoria']
    return render_template('index.html',title='Welcome', members=users)

app.run(host='0.0.0.0', port=81)