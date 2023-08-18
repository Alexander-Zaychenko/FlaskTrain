from flask import Flask, redirect, render_template
import os
import psycopg2

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/home', code=302)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/fun')
def fun():
    return render_template('fun.html')


@app.route('/home/branch')
def branch():
    return render_template('branch.html')


@app.route('/post/<id>')
def post(id):
    return f'Hello {id}'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
