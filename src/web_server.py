from datetime import datetime, timedelta
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from news import Nnews
from dbpy import Data, Base
from dbpyt import Datab, Based
from flask import url_for
import jwt
from flask.json import jsonify
import os

os.environ["CUDA_VISIBLE_DEVICES"]="0,1"
scrap = Nnews()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty123@localhost/py4'
datab = SQLAlchemy(app)
tok = ''

@app.route('/')
def build_login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
    usern = request.form["username"]
    passw = request.form["password"]
    pres = datab.session.query(Datab).all()
    for prow in pres:
        if usern == prow.login and passw == prow.password:
            log = usern
            token = jwt.encode({'user':log, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
            user = datab.session.query(Datab).filter_by(login = log).first()
            user.token = token
            datab.session.commit()
            return  redirect('/input')
        else:
            continue
    return render_template('login.html')

@app.route('/input')
def my_form():
    return render_template('news.html')

@app.route('/input', methods=['POST'])
def my_form_post():
    sh = []
    text = request.form['text']
    for x in range(5):
        sh.extend(scrap.newspull(text, x+1))
    for x in range(5):
        upd = datab.session.query(Data).filter_by(news_id = (x+1)).first()
        upd.news_text = sh[(x*2)+1]
        datab.session.commit()
    print(sh)
    return render_template('news.html', h1=sh[0], text1=sh[1], h2=sh[2], text2=sh[3], h3=sh[4], text3=sh[5], h4=sh[6], text4=sh[7], h5=sh[8], text5=sh[9])

def start():
    app.run(debug=True)