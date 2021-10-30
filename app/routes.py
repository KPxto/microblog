from flask import render_template
from app import app


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