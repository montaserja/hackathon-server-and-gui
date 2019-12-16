from flask import Flask,render_template
from flask import request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def index():
    return render_template('index.html')
