from flask import Flask, render_template, redirect, url_for
# import data
from data import *
app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html',title='Git-Cheat-Sheet',data=data)



if __name__=='__main__':
    app.run(debug=True)
