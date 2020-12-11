from flask import render_template, flash, redirect, url_for
from myapp import app
from myapp.forms import LoginForm


# Home page maybe with some instructions / login

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nathan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


# contacts index page



# add contact routes

# edit contact routes

# delete contact

# contact show page / add comment

# edit comment

# delete comment




