from flask import Flask, session, request, escape, redirect, url_for

app = Flask(__name__)
app.secret_key = 'huydheeyjkhn'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'> click here to logout </a></b>"
    return "you are not logged in <br><a href = 'login'>" + "click here to log in</a>"

@app.route('/login', methods  = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''

    <form action = "" method = "POST">
        <p><input type = text name = username /></p>
        <p><input type = submit value = login /></p>
    </form>     
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=81)