from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'alfred'
    }
    
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie FTW!'
        }
    ]

    # render template requires template_name & context params
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash -> show message to user
        flash(f'Log in requested for {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')

    return render_template('login.html', title='Sign in', form=form)