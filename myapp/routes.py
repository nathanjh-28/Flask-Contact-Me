from flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nathan'}
    return render_template('index.html', title='Home', user=user)