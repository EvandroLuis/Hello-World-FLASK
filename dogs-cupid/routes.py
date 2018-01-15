import os

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from login import db

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('HomePage.html', title='Dogs Cupid',)


@app.route('/logon', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    database = db.get_db()
    database.execute('insert into owner (name, email, password, telephone, country, city) values (?, ?, ?, ?, ?, ?)',
                 [request.form['name'], request.form['email'], request.form['password'], request.form['telephone'],
                  request.form['country'], request.form['city']])
    database.commit()
    return flash('Your account have been created')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home_page'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('/'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT')) or 5000
    app.run(port=port, host='0.0.0.0')

