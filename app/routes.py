from flask import render_template, flash, redirect
from werkzeug.utils import redirect
from app import app
from app.form import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Kaio'}
    posts = [
        {
            'author': {'username': 'Zé'},
            'body':'Tá tudo caro na feira! Deu zulivre'
        },
        {
            'author':{'username': 'Maria'},
            'body': 'Agora vou ter q dá a xavasca pra arrumar dindin kkk'
        }
    ]
    return render_template(
        'index.html', 
        title='Kaio', 
        user=user, 
        posts=posts
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():    
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)

